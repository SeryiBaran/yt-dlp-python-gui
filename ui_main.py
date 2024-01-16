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
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 819)
        font = QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icon.ico", QSize(), QIcon.Normal, QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(32)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.plainTextEdit_urls = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_urls.setObjectName(u"plainTextEdit_urls")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_urls.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_urls.setSizePolicy(sizePolicy)
        self.plainTextEdit_urls.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout.addWidget(self.plainTextEdit_urls)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_download_directory = QPushButton(self.centralwidget)
        self.button_download_directory.setObjectName(u"button_download_directory")

        self.horizontalLayout.addWidget(self.button_download_directory)

        self.label_download_directory = QLabel(self.centralwidget)
        self.label_download_directory.setObjectName(u"label_download_directory")

        self.horizontalLayout.addWidget(self.label_download_directory)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.check_download_playlist = QCheckBox(self.centralwidget)
        self.check_download_playlist.setObjectName(u"check_download_playlist")
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

        self.verticalLayout.addWidget(self.check_download_playlist)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.comboBox_video_size = QComboBox(self.centralwidget)
        self.comboBox_video_size.setObjectName(u"comboBox_video_size")
        self.comboBox_video_size.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.comboBox_video_size)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_6)

        self.pushButton_download = QPushButton(self.centralwidget)
        self.pushButton_download.setObjectName(u"pushButton_download")

        self.verticalLayout.addWidget(self.pushButton_download)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_5)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.plainTextEdit_logs = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_logs.setObjectName(u"plainTextEdit_logs")
        self.plainTextEdit_logs.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.plainTextEdit_logs.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit_logs)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0438\u0432\u0430\u043b\u043a\u0430 \u0441 YouTube (\u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441 \u0434\u043b\u044f yt-dlp)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0438\u0432\u0430\u043b\u043a\u0430 \u0441 YouTube", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>(\u0418\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441 \u0434\u043b\u044f yt-dlp)</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0430\u0434\u0440\u0435\u0441 \u0432\u0438\u0434\u0435\u043e/\u043f\u043b\u0435\u0439\u043b\u0438\u0441\u0442\u0430: (\u043c\u043e\u0436\u043d\u043e \u0432\u0441\u0442\u0430\u0432\u043b\u044f\u0442\u044c \u043c\u043d\u043e\u0433\u043e \u0441\u0441\u044b\u043b\u043e\u043a,</p><p>\u043a\u0430\u0436\u0434\u0443\u044e \u043d\u0430 \u043d\u043e\u0432\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0435)</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0430\u043f\u043a\u0443 \u0434\u043b\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438:</p></body></html>", None))
        self.button_download_directory.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443", None))
        self.label_download_directory.setText(QCoreApplication.translate("MainWindow", u"C:/Users/ivan/Downloads", None))
        self.check_download_playlist.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c \u043f\u043b\u0435\u0439\u043b\u0438\u0441\u0442", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u0438\u0434\u0435\u043e:", None))
        self.pushButton_download.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0432\u043e\u0434:", None))
    # retranslateUi

