import datetime
import sys
import os
import userfolders
import yt_dlp
import configparser
import json

from PySide6 import QtCore, QtGui

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QDialog,
    QPushButton,
)
from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QMainWindow
import qdarktheme

from ui_main import Ui_MainWindow
from ui_about import Ui_AboutWindow


def resource_path(relative_path):
    if hasattr(sys, "_MEIP"):
        return os.path.join(sys._MEIP, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


VERSION = "NOTFOUND"
YT_DLP_VERSION = "NOTFOUND"

with open(resource_path("versions.json")) as f:
    d = json.load(f)
    VERSION = d["app"]
    YT_DLP_VERSION = d["yt_dlp"]

VERSION_LABEL_VALUE = f"""Версия этой программы - {VERSION}
Версия yt-dlp - {YT_DLP_VERSION}"""

ini_config = configparser.ConfigParser()
try:
    ini_config.read("yt-dlp-python-gui.ini")
except:
    print("[INFO]: cannot read yt-dlp-python-gui.ini")


def get_parameter(parameter_name):
    if ini_config.has_section("settings") and ini_config.has_option(
        "settings", parameter_name
    ):
        return ini_config.get("settings", parameter_name)
    return False


def set_parameter(parameter_name, value):
    ini_config.set("settings", parameter_name, value)


download_finished = True
errors = []

urls = []
download_directory = get_parameter("download_directory") or userfolders.get_downloads()
video_sizes = ("360", "480", "720", "1080")
video_size = get_parameter("video_size") or "360"
big_ui = (False) if (get_parameter("big_ui") == "False") else (True)
download_playlist = get_parameter("download_playlist") == "True" or False
download_only_music = get_parameter("download_only_music") == "True" or False


def get_params_json():
    return {
        "download_directory": download_directory,
        "video_size": video_size,
        "big_ui": big_ui,
        "download_playlist": download_playlist,
        "download_only_music": download_only_music,
    }


def write_config():
    if not ini_config.has_section("settings"):
        ini_config.add_section("settings")

    set_parameter("download_directory", download_directory)
    set_parameter("video_size", video_size)
    set_parameter("big_ui", str(big_ui))
    set_parameter("download_playlist", str(download_playlist))
    set_parameter("download_only_music", str(download_only_music))

    with open("yt-dlp-python-gui.ini", "w") as configfile:
        ini_config.write(configfile)


def write_history():
    with open("yt-dlp-python-gui__URL_HISTORY.txt", "a") as historyfile:
        historyfile.write(
            "\nSTART " + datetime.datetime.now().isoformat() + " IN REGIONAL TIME;\n"
        )
        historyfile.write("\nPARAMS " + json.dumps(get_params_json()) + ";\n")
        historyfile.write("\nURLS:::\n" + "\n".join(urls).strip() + "\n")
        historyfile.write("\nEND;\n")


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
        errors.append(msg)


class YoutubeDownload(QtCore.QThread):
    messageSignal = QtCore.Signal(str)
    finishedSignal = QtCore.Signal()
    errorSignal = QtCore.Signal(str)

    def __init__(self, urls, ydl_opts, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.urls = urls
        self.ydl_opts = ydl_opts
        self._is_running = True

    def run(self):
        self.messageSignal.emit("STARTED")
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                ydl.download(self.urls)
                if self._is_running:
                    self.messageSignal.emit("ENDED")
        except Exception as e:
            self.errorSignal.emit(str(e))
        self.finishedSignal.emit()

    def my_stop(self):
        self._is_running = False
        global download_finished
        download_finished = True
        self.messageSignal.emit("ENDED")
        self.terminate()
        self.quit()


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

        if big_ui:
            self.setWindowState(QtCore.Qt.WindowMaximized)
            self.resize(620, 720)

            font = QFont()
            font.setPointSize(14)
            QApplication.setFont(font)
            self.setStyleSheet("font-size: 14;")

            font1 = QFont()
            font1.setPointSize(20)
            self.ui.label_13.setFont(font1)

            self.ui.plainTextEdit_urls.setMaximumSize(QSize(16777215, 140))
            self.ui.check_download_playlist.setStyleSheet(
                "QCheckBox::indicator { width: 36px; height: 36px;}"
            )
            self.ui.check_download_only_music.setStyleSheet(
                "QCheckBox::indicator { width: 36px; height: 36px;}"
            )
            self.ui.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 603, 859))
            self.ui.plainTextEdit_urls.setMaximumSize(QSize(16777215, 140))

            font3 = QFont()
            font3.setPointSize(9)
            self.ui.plainTextEdit_logs.setFont(font3)

        self.ui.aboutButton.clicked.connect(self.open_about_window)

        self.ui.button_paste_from_clipboard.clicked.connect(
            self.handle_button_paste_from_clipboard
        )
        self.ui.plainTextEdit_urls.textChanged.connect(self.handle_plainTextEdit_urls)

        self.ui.button_download_directory.clicked.connect(
            self.handle_download_directory_select
        )

        self.ui.lineEdit_download_directory.setText(download_directory)

        self.ui.comboBox_video_size.addItems(video_sizes)
        self.ui.comboBox_video_size.currentTextChanged.connect(
            self.handle_comboBox_video_size
        )
        self.ui.comboBox_video_size.setCurrentText(video_size)

        self.ui.check_big_ui.clicked.connect(self.handle_check_big_ui)
        self.ui.check_big_ui.setChecked(big_ui)

        self.ui.check_download_playlist.clicked.connect(
            self.handle_check_download_playlist
        )
        self.ui.check_download_playlist.setChecked(download_playlist)

        self.ui.check_download_only_music.clicked.connect(
            self.handle_check_download_only_music
        )
        self.ui.check_download_only_music.setChecked(download_only_music)

        self.ui.pushButton_download.clicked.connect(self.handle_submit)
        self.ui.pushButton_cancel.clicked.connect(self.cancel_download)

    def cancel_download(self):
        if hasattr(self, "thread"):
            self.thread.my_stop()
            self.log("[INFO] ЗАГРУЗКА ПРЕРВАНА ПОЛЬЗОВАТЕЛЕМ")
            self.ui.pushButton_download.setDisabled(False)
            self.ui.pushButton_download.setText("Скачать")

    def log(self, message):
        self.ui.plainTextEdit_logs.appendPlainText(str(message))

    def open_about_window(self):
        self.about_window = AboutWindow()

        if big_ui:
            font2 = QFont()
            font2.setPointSize(20)
            self.about_window.ui.label.setFont(font2)
            self.about_window.ui.label_2.setFont(font2)

        self.about_window.show()

    def handle_button_paste_from_clipboard(self):
        from_clipboard = QtGui.QGuiApplication.clipboard().text()

        self.ui.plainTextEdit_urls.appendPlainText("\n" + from_clipboard + "\n")
        self.handle_plainTextEdit_urls()

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
                self.ui.lineEdit_download_directory.setText(download_directory)
                write_config()

    def handle_comboBox_video_size(self, value):
        global video_size
        video_size = value
        write_config()

    def handle_check_big_ui(self):
        global big_ui
        big_ui = self.ui.check_big_ui.isChecked()
        write_config()

    def handle_check_download_playlist(self):
        global download_playlist
        download_playlist = self.ui.check_download_playlist.isChecked()
        write_config()

    def handle_check_download_only_music(self):
        global download_only_music
        download_only_music = self.ui.check_download_only_music.isChecked()
        write_config()

    def handle_download_state_changed(self, msg):
        global download_finished
        if msg == "STARTED":
            download_finished = False

            self.ui.pushButton_download.setDisabled(not download_finished)
            self.ui.pushButton_download.setText("Идет скачивание...")
            self.log("[INFO] Началось скачивание")
        elif msg == "ENDED":
            file_list = os.listdir(download_directory)

            for file in file_list:
                if file.endswith(".part"):
                    try:
                        os.remove(os.path.join(download_directory, file))
                    except:
                        pass

            download_finished = True

            self.ui.pushButton_download.setDisabled(not download_finished)
            self.ui.pushButton_download.setText("Скачать")
            self.log("[INFO] Скачивание завершено")
            if len(errors) > 0:
                self.log(f"[ERROR] Во время скачивания произошли следующие ошибки:")
                self.log("\n".join(errors))
                self.log(f"[ERROR] ВО ВРЕМЯ СКАЧИВАНИЯ ПРОИЗОШЛИ ОШИБКИ!")

    def handle_submit(self):
        if len(urls) == 0:
            self.log("ВВЕДИТЕ АДРЕС(А)!")
        else:
            global errors
            errors = []
            logger = MyLogger()
            logger.messageSignal.connect(self.ui.plainTextEdit_logs.appendPlainText)
            self.log(f"Заданы параметры: {json.dumps(get_params_json())}")
            write_history()
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
                "format_sort": [f"res:{video_size}", f"ext:mp4:m4a", f"vcodec:h264"],
                "noplaylist": not download_playlist,
                "paths": {"home": download_directory},
                "ignoreerrors": True,
            }

            if download_only_music:
                ydl_opts["format"] = "bestaudio/best"
                ydl_opts["postprocessors"].append(
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                )

            self.thread = YoutubeDownload(urls, ydl_opts)
            self.thread.messageSignal.connect(self.handle_download_state_changed)
            # self.thread.finishedSignal.connect(self.thread.deleteLater)
            def err(e):
                errors.append(e)
                self.log(e)
            self.thread.errorSignal.connect(err)
            self.thread.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("auto")

    window = App()
    window.show()

    sys.exit(app.exec())
