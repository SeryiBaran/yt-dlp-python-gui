# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        if not AboutWindow.objectName():
            AboutWindow.setObjectName(u"AboutWindow")
        AboutWindow.resize(400, 282)
        icon = QIcon()
        icon.addFile(u":/icons/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        AboutWindow.setWindowIcon(icon)
        AboutWindow.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.horizontalLayout = QHBoxLayout(AboutWindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(AboutWindow)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.versionsLabel = QLabel(self.widget)
        self.versionsLabel.setObjectName(u"versionsLabel")

        self.verticalLayout_2.addWidget(self.versionsLabel)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setWordWrap(True)
        self.label_5.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.label_5)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(self.widget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(AboutWindow)

        QMetaObject.connectSlotsByName(AboutWindow)
    # setupUi

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(QCoreApplication.translate("AboutWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.label.setText(QCoreApplication.translate("AboutWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.label_3.setText(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p>\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b - YTPDown (yt-dlp-python-gui). (<a href=\"https://github.com/SeryiBaran/yt-dlp-python-gui\"><span>GitHub</span></a>)</p></body></html>", None))
        self.versionsLabel.setText(QCoreApplication.translate("AboutWindow", u"\u0412\u0435\u0440\u0441\u0438\u044f \u044d\u0442\u043e\u0439 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b - {VERSION}\n"
"\u0412\u0435\u0440\u0441\u0438\u044f yt-dlp - {YT_DLP_VERSION}", None))
        self.label_4.setText(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p>\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a - SeryiBaran (<a href=\"https://seryibaran.github.io\"><span>seryibaran.github.io</span></a>)</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("AboutWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 FFmpeg", None))
        self.label_5.setText(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p>\u0414\u043b\u044f \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u044f \u0432\u0438\u0434\u0435\u043e \u043d\u0443\u0436\u0435\u043d FFmpeg. \u0415\u0433\u043e \u043d\u0443\u0436\u043d\u043e \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0447\u0435\u0440\u0435\u0437 Scoop (<a href=\"https://scoop.sh\"><span>scoop.sh</span></a>), \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u043c\u043e\u0435\u0433\u043e \u043f\u043e\u043b\u0443\u0440\u0430\u0431\u043e\u0447\u0435\u0433\u043e \u043a\u0430\u043b\u043e\u0432\u043e\u0433\u043e \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0449\u0438\u043a\u0430 (<a href=\"https://github.com/SeryiBaran/ffmpeg_installer\"><span>github.com/SeryiBaran/ffmpeg_installer</span></a>) \u0438\u043b\u0438 \u043f\u043e \u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f\u043c \u0432 \u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442\u0435.</p></body></html>", None))
    # retranslateUi

