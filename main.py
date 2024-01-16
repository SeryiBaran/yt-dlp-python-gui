import sys
from pathlib import Path
from win32com.shell import shell, shellcon
import yt_dlp

from PySide6 import QtCore

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QFileDialog,
    QGridLayout,
    QPushButton,
    QLabel,
    QListWidget,
)

from ui_main import Ui_MainWindow

urls = []
download_directory = shell.SHGetKnownFolderPath(shellcon.FOLDERID_Downloads)
download_playlist = False
video_sizes = ("360", "480", "720")
video_size = "360"


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


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.plainTextEdit_urls.textChanged.connect(self.handle_plainTextEdit_urls)
        self.ui.button_download_directory.clicked.connect(
            self.handle_download_directory_select
        )
        self.ui.check_download_playlist.clicked.connect(
            self.handle_check_download_playlist
        )
        self.ui.pushButton_download.clicked.connect(self.handle_submit)

        self.ui.label_download_directory.setText(download_directory)

        self.ui.comboBox_video_size.addItems(video_sizes)
        self.ui.comboBox_video_size.currentTextChanged.connect(
            self.handle_comboBox_video_size
        )

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

    def handle_check_download_playlist(self):
        global download_playlist
        download_playlist = self.ui.check_download_playlist.isChecked()

    def handle_comboBox_video_size(self, value):
        global video_size
        video_size = value

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
                "compat_opts": "filename",
                "format_sort": [f"res:{video_size}"],
                "noplaylist": not download_playlist,
                "paths": {"home": download_directory},
            }
            self.thread = YoutubeDownload(urls, ydl_opts)
            self.thread.start()
            self.thread.messageSignal.connect(self.handle_download_state_changed)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = App()
    window.show()

    sys.exit(app.exec())
