import sys
from win32com.shell import shell, shellcon
import yt_dlp
import configparser

from PySide6 import QtCore

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QDialog
)

BIG_UI = False # Change to `False` if need standard compact 9px ui
from ui_main import Ui_MainWindow # Standard compact 9px ui
# from ui_main__big_ui import Ui_MainWindow # Big ui

from ui_about import Ui_AboutWindow

VERSION = "1.0.5"
YT_DLP_VERSION = "2023.12.30"

VERSION_LABEL_VALUE = f"""Версия этой программы - {VERSION}
Версия yt-dlp - {YT_DLP_VERSION}"""

ini_config = configparser.ConfigParser()
try:
    ini_config.read("yt-dlp-python-gui.ini")
except:
    print("INFO: cannot read yt-dlp-python-gui.ini")


def get_parameter(parameter_name):
    if ini_config.has_section("settings") and ini_config.has_option(
        "settings", parameter_name
    ):
        return ini_config.get("settings", parameter_name)
    return False


def set_parameter(parameter_name, value):
    ini_config.set("settings", parameter_name, value)


urls = []
download_directory = get_parameter("download_directory") or shell.SHGetKnownFolderPath(
    shellcon.FOLDERID_Downloads
)
download_playlist = get_parameter("download_playlist") == "True" or False
video_sizes = ("360", "480", "720", "1080")
video_size = get_parameter("video_size") or "360"


def write_config():
    if not ini_config.has_section("settings"):
        ini_config.add_section("settings")

    set_parameter("download_directory", download_directory)
    set_parameter("download_playlist", str(download_playlist))
    set_parameter("video_size", video_size)

    with open("yt-dlp-python-gui.ini", "w") as configfile:
        ini_config.write(configfile)


write_config()


class MyLogger(QtCore.QObject):
    messageSignal = QtCore.Signal(str)

    def info(self, msg):
        self.messageSignal.emit(msg)

    def debug(self, msg):
        self.messageSignal.emit(msg)

    def warning(self, msg):
        self.messageSignal.emit(msg)

    def error(self, msg):
        self.messageSignal.emit(msg)


class YoutubeDownload(QtCore.QThread):
    messageSignal = QtCore.Signal(str)

    def __init__(
        self,
        urls,
        ydl_opts,
        *args,
        **kwargs,
    ):
        QtCore.QThread.__init__(self, *args, **kwargs)
        self.urls = urls
        self.ydl_opts = ydl_opts

    def run(self):
        self.messageSignal.emit("STARTED")
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download(self.urls)

            self.messageSignal.emit("ENDED")


def yt_dlp_hook(d):
    if d["status"] == "finished":
        global download_finished
        download_finished = True


class AboutWindow(QDialog):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.window = Ui_AboutWindow()
        self.ui = self.window
        self.ui.setupUi(self)

        self.ui.versionsLabel.setText(VERSION_LABEL_VALUE)

        self.ui.buttonBox.accepted.connect(self.close)


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.window = Ui_MainWindow()
        self.ui = self.window
        self.ui.setupUi(self)
        if BIG_UI:
            self.setWindowState(QtCore.Qt.WindowMaximized)

        self.ui.plainTextEdit_urls.textChanged.connect(self.handle_plainTextEdit_urls)
        self.ui.button_download_directory.clicked.connect(
            self.handle_download_directory_select
        )
        self.ui.check_download_playlist.clicked.connect(
            self.handle_check_download_playlist
        )
        self.ui.check_download_playlist.setChecked(download_playlist)
        self.ui.pushButton_download.clicked.connect(self.handle_submit)

        self.ui.label_download_directory.setText(download_directory)

        self.ui.comboBox_video_size.addItems(video_sizes)
        self.ui.comboBox_video_size.currentTextChanged.connect(
            self.handle_comboBox_video_size
        )
        self.ui.comboBox_video_size.setCurrentText(video_size)

        self.ui.aboutButton.clicked.connect(self.open_about_window)

    def log(self, message):
        self.ui.plainTextEdit_logs.appendPlainText(str(message))

    def handle_plainTextEdit_urls(self):
        lines_from_input = self.ui.plainTextEdit_urls.toPlainText().split("\n")
        cleared_lines = []
        for elem in lines_from_input:
            if elem != "":
                cleared_lines.append(elem)
        global urls
        urls = cleared_lines

    def handle_download_directory_select(self):
        global download_directory
        dialog = QFileDialog(self)
        dialog.setDirectory(download_directory)
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                download_directory = filenames[0]
                self.ui.label_download_directory.setText(download_directory)
                print("from class: ", download_directory)
                write_config()

    def handle_check_download_playlist(self):
        global download_playlist
        download_playlist = self.ui.check_download_playlist.isChecked()
        write_config()

    def handle_comboBox_video_size(self, value):
        global video_size
        video_size = value
        write_config()

    def handle_download_state_changed(self, msg):
        if msg == "STARTED":
            self.ui.pushButton_download.setDisabled(True)
            self.ui.pushButton_download.setText("Идет скачивание...")
            self.log("[INFO] Началось скачивание")
        elif msg == "ENDED":
            self.ui.pushButton_download.setDisabled(False)
            self.ui.pushButton_download.setText("Скачать")
            self.log("[INFO] Скачивание завершено")

    def handle_submit(self):
        if len(urls) == 0:
            self.log("ВВЕДИТЕ АДРЕС!")
        else:
            logger = MyLogger()
            logger.messageSignal.connect(self.ui.plainTextEdit_logs.appendPlainText)
            self.log(
                f"Заданы параметры: download_playlist = {download_playlist}, urls = {urls}, download_directory = {download_directory}, video_size = {video_size}"
            )
            ydl_opts = {
                "logger": logger,
                "progress_hooks": [yt_dlp_hook],
                # "compat_opts": {"filename-sanitization"},
                "postprocessors": [
                    {
                        "actions": [
                            (
                                yt_dlp.postprocessor.metadataparser.MetadataParserPP.replacer,
                                "title",
                                # https://en.wikipedia.org/wiki/NTFS restrictions /\:*"?<>| plus `'
                                "[\/\\\:\*\"\?\<\>\|\`']",
                                "_",
                            )
                        ],
                        "key": "MetadataParser",
                        "when": "pre_process",
                    },
                    {
                        "key": "FFmpegConcat",
                        "only_multi_video": True,
                        "when": "playlist",
                    },
                ],
                "format_sort": [f"res:{video_size}", f"ext:mp4:m4a"],
                "noplaylist": not download_playlist,
                "paths": {"home": download_directory}
            }
            self.thread = YoutubeDownload(urls, ydl_opts)
            self.thread.start()
            self.thread.messageSignal.connect(self.handle_download_state_changed)

    def open_about_window(self):
        self.about_window = AboutWindow()
        self.about_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = App()
    window.show()

    sys.exit(app.exec())
