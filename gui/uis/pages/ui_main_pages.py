# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesJqGnhJ.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from qt_core import *
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
                               QHBoxLayout, QLabel, QScrollArea, QSizePolicy,
                               QStackedWidget, QVBoxLayout, QWidget)
from .py_left_menu_button import PyLeftMenuButton


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(763, 637)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = QFrame(self.page_1)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(300, 150))
        self.welcome_base.setMaximumSize(QSize(300, 150))
        self.welcome_base.setFrameShape(QFrame.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Raised)
        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(300, 120))
        self.logo.setMaximumSize(QSize(300, 120))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.center_page_layout.addWidget(self.logo)

        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.center_page_layout.addWidget(self.label)

        self.page_1_layout.addWidget(self.welcome_base, 0, Qt.AlignHCenter)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 232, 265))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)

        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.verticalLayout.addLayout(self.row_5_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_2)

        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
                                  "	font-size: 16pt;\n"
                                  "}")
        self.gridLayout = QGridLayout(self.page_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.page_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_button_CAD = QFrame(self.page_3)
        self.frame_button_CAD.setObjectName(u"frame_button_CAD")
        self.frame_button_CAD.setMinimumSize(QSize(0, 40))
        self.frame_button_CAD.setMaximumSize(QSize(16777215, 40))
        self.frame_button_CAD.setFrameShape(QFrame.NoFrame)
        self.frame_button_CAD.setFrameShadow(QFrame.Raised)
        self.btn_CAD_layout = QHBoxLayout(self.frame_button_CAD)
        self.btn_CAD_layout.setSpacing(0)
        self.btn_CAD_layout.setObjectName(u"btn_CAD_layout")
        self.btn_CAD_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.frame_button_CAD, 0, 1, 1, 1)

        self.frame_2 = QFrame(self.page_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.frame_2, 0, 2, 1, 1)

        self.frame_button_fulldisk = QFrame(self.page_3)
        self.frame_button_fulldisk.setObjectName(u"frame_button_fulldisk")
        self.frame_button_fulldisk.setMinimumSize(QSize(0, 40))
        self.frame_button_fulldisk.setMaximumSize(QSize(16777215, 40))
        self.frame_button_fulldisk.setFrameShape(QFrame.NoFrame)
        self.frame_button_fulldisk.setFrameShadow(QFrame.Raised)
        self.btn_fulldisk_layout = QVBoxLayout(self.frame_button_fulldisk)
        self.btn_fulldisk_layout.setSpacing(0)
        self.btn_fulldisk_layout.setObjectName(u"btn_fulldisk_layout")
        self.btn_fulldisk_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.frame_button_fulldisk, 0, 3, 1, 1)

        self.frame_3 = QFrame(self.page_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.frame_3, 0, 4, 1, 1)

        self.frame_button_dirdisk = QFrame(self.page_3)
        self.frame_button_dirdisk.setObjectName(u"frame_button_dirdisk")
        self.frame_button_dirdisk.setMinimumSize(QSize(0, 40))
        self.frame_button_dirdisk.setMaximumSize(QSize(16777215, 40))
        self.frame_button_dirdisk.setFrameShape(QFrame.NoFrame)
        self.frame_button_dirdisk.setFrameShadow(QFrame.Raised)
        self.btn_dirdisk_layout = QVBoxLayout(self.frame_button_dirdisk)
        self.btn_dirdisk_layout.setSpacing(0)
        self.btn_dirdisk_layout.setObjectName(u"btn_dirdisk_layout")
        self.btn_dirdisk_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.frame_button_dirdisk, 0, 5, 1, 1)

        self.scroll_result = QFrame(self.page_3)
        self.scroll_result.setObjectName(u"scroll_result")
        self.scroll_result.setMinimumSize(QSize(0, 40))
        self.scroll_result.setMaximumSize(QSize(16777215, 16777215))
        self.scroll_result.setFrameShape(QFrame.NoFrame)
        self.scroll_result.setFrameShadow(QFrame.Raised)
        self.scroll_result_layout = QFormLayout(self.scroll_result)
        self.scroll_result_layout.setObjectName(u"scroll_result_layout")
        self.scroll_result_layout.setHorizontalSpacing(0)
        self.scroll_result_layout.setVerticalSpacing(0)
        self.scroll_result_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.scroll_result, 1, 0, 2, 3)

        self.frame_Progress_Circle = QFrame(self.page_3)
        self.frame_Progress_Circle.setObjectName(u"frame_Progress_Circle")
        self.frame_Progress_Circle.setFrameShape(QFrame.NoFrame)
        self.frame_Progress_Circle.setFrameShadow(QFrame.Raised)
        self.frame_Progress_Circle.setLineWidth(0)
        self.formLayout = QFormLayout(self.frame_Progress_Circle)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.frame_Progress_Circle, 1, 3, 1, 3)

        self.frame_4 = QFrame(self.page_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_4, 2, 3, 2, 3)

        self.frame_button_scan = QFrame(self.page_3)
        self.frame_button_scan.setObjectName(u"frame_button_scan")
        self.frame_button_scan.setMinimumSize(QSize(0, 40))
        self.frame_button_scan.setMaximumSize(QSize(16777215, 40))
        self.frame_button_scan.setFrameShape(QFrame.NoFrame)
        self.frame_button_scan.setFrameShadow(QFrame.Raised)
        self.btn_scan_layout = QHBoxLayout(self.frame_button_scan)
        self.btn_scan_layout.setSpacing(0)
        self.btn_scan_layout.setObjectName(u"btn_scan_layout")
        self.btn_scan_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.frame_button_scan, 3, 0, 1, 3)

        self.pages.addWidget(self.page_3)

        self.main_pages_layout.addWidget(self.pages)

        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(2)
        QMetaObject.connectSlotsByName(MainPages)

    # setupUi




    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Welcome To Liliac-Virus-Killer", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"正在扫描...", None))
        self.description_label.setText(QCoreApplication.translate("MainPages", u"选择扫描方式：\n"
                                                                               "自动检测CAD安装路径扫描/全局扫描/上传路径定向扫描", None))
        self.label_2.setText(QCoreApplication.translate("MainPages",
                                                        u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">CAD\u626b\u63cf</span></p></body></html>",
                                                        None))
        self.label_3.setText(QCoreApplication.translate("MainPages",
                                                        u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u5168\u5c40\u626b\u63cf</span></p></body></html>",
                                                        None))
        self.label_4.setText(QCoreApplication.translate("MainPages",
                                                        u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u5b9a\u5411\u626b\u63cf</span></p></body></html>",
                                                        None))
    # retranslateUi
