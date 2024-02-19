# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QMainWindow, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(640, 780)
        font = QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icon.ico", QSize(), QIcon.Normal, QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(640, 16777215))
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 623, 783))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        font1 = QFont()
        font1.setPointSize(26)
        self.label_13.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_13)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.aboutButton = QPushButton(self.scrollAreaWidgetContents)
        self.aboutButton.setObjectName(u"aboutButton")

        self.horizontalLayout_4.addWidget(self.aboutButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.line_18 = QFrame(self.scrollAreaWidgetContents)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_18)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_15)

        self.plainTextEdit_urls = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_urls.setObjectName(u"plainTextEdit_urls")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_urls.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_urls.setSizePolicy(sizePolicy)
        self.plainTextEdit_urls.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout_3.addWidget(self.plainTextEdit_urls)

        self.line_16 = QFrame(self.scrollAreaWidgetContents)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_16)

        self.label_18 = QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_3.addWidget(self.label_18)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_download_directory = QPushButton(self.scrollAreaWidgetContents)
        self.button_download_directory.setObjectName(u"button_download_directory")

        self.horizontalLayout_3.addWidget(self.button_download_directory)

        self.label_download_directory = QLabel(self.scrollAreaWidgetContents)
        self.label_download_directory.setObjectName(u"label_download_directory")

        self.horizontalLayout_3.addWidget(self.label_download_directory)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.line_14 = QFrame(self.scrollAreaWidgetContents)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_14)

        self.check_download_playlist = QCheckBox(self.scrollAreaWidgetContents)
        self.check_download_playlist.setObjectName(u"check_download_playlist")
        self.check_download_playlist.setFont(font)
        self.check_download_playlist.setStyleSheet(u"QCheckBox::indicator\n"
"{\n"
"	width: 50px;\n"
"	height: 50px;\n"
"}\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image: url(:/icons/CarbonCheckboxChecked.svg);\n"
"}\n"
"QCheckBox::indicator:unchecked\n"
"{\n"
"    image: url(:/icons/CarbonCheckbox.svg);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.check_download_playlist)

        self.line_13 = QFrame(self.scrollAreaWidgetContents)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_13)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout.addWidget(self.label_14)

        self.comboBox_video_size = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_video_size.setObjectName(u"comboBox_video_size")
        self.comboBox_video_size.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.comboBox_video_size)

        self.horizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_1)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(9)
        self.label.setFont(font2)
        self.label.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label)

        self.line_15 = QFrame(self.scrollAreaWidgetContents)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_15)

        self.pushButton_download = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_download.setObjectName(u"pushButton_download")

        self.verticalLayout_3.addWidget(self.pushButton_download)

        self.line_17 = QFrame(self.scrollAreaWidgetContents)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_17)

        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_3.addWidget(self.label_17)

        self.plainTextEdit_logs = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_logs.setObjectName(u"plainTextEdit_logs")
        self.plainTextEdit_logs.setMinimumSize(QSize(0, 180))
        self.plainTextEdit_logs.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.plainTextEdit_logs.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.plainTextEdit_logs)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0438\u0432\u0430\u043b\u043a\u0430 \u0441 YouTube (\u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441 \u0434\u043b\u044f yt-dlp)", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0438\u0432\u0430\u043b\u043a\u0430 \u0441 YouTube", None))
        self.aboutButton.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0430\u0434\u0440\u0435\u0441 \u0432\u0438\u0434\u0435\u043e/\u043f\u043b\u0435\u0439\u043b\u0438\u0441\u0442\u0430 (\u043c\u043e\u0436\u043d\u043e \u0432\u0441\u0442\u0430\u0432\u043b\u044f\u0442\u044c \u043c\u043d\u043e\u0433\u043e \u0441\u0441\u044b\u043b\u043e\u043a, \u043a\u0430\u0436\u0434\u0443\u044e \u043d\u0430 \u043d\u043e\u0432\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0435):</p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0430\u043f\u043a\u0443 \u0434\u043b\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438:</p></body></html>", None))
        self.button_download_directory.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443", None))
        self.label_download_directory.setText(QCoreApplication.translate("MainWindow", u"C:/Users/ivan/Downloads", None))
        self.check_download_playlist.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c \u043f\u043b\u0435\u0439\u043b\u0438\u0441\u0442", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u0438\u0434\u0435\u043e:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0438\u043c\u0430\u043d\u0438\u0435: \u0434\u043b\u044f \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u044f \u0432\u0438\u0434\u0435\u043e \u0432 1080 \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u0442\u0441\u044f \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c FFmpeg. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e scoop. \u0418\u043d\u0430\u0447\u0435 \u0432\u043c\u0435\u0441\u0442\u043e 1080 \u043c\u043e\u0436\u0435\u0442 \u043a\u0430\u0447\u0430\u0442\u044c\u0441\u044f 720.", None))
        self.pushButton_download.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0432\u043e\u0434:", None))
    # retranslateUi

