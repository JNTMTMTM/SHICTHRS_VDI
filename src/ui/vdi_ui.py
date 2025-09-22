# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vdi_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableView, QWidget)

class Ui_vdi(object):
    def setupUi(self, vdi):
        if not vdi.objectName():
            vdi.setObjectName(u"vdi")
        vdi.resize(800, 490)
        self.tv_main = QTableView(vdi)
        self.tv_main.setObjectName(u"tv_main")
        self.tv_main.setGeometry(QRect(10, 21, 781, 401))
        self.lb_base_path = QLabel(vdi)
        self.lb_base_path.setObjectName(u"lb_base_path")
        self.lb_base_path.setGeometry(QRect(10, 0, 781, 21))
        self.pbtn_read_base_path = QPushButton(vdi)
        self.pbtn_read_base_path.setObjectName(u"pbtn_read_base_path")
        self.pbtn_read_base_path.setGeometry(QRect(10, 430, 131, 23))
        self.pbtn_read_vdi_file = QPushButton(vdi)
        self.pbtn_read_vdi_file.setObjectName(u"pbtn_read_vdi_file")
        self.pbtn_read_vdi_file.setEnabled(False)
        self.pbtn_read_vdi_file.setGeometry(QRect(10, 460, 131, 23))
        self.li_div_left = QFrame(vdi)
        self.li_div_left.setObjectName(u"li_div_left")
        self.li_div_left.setGeometry(QRect(140, 430, 41, 51))
        self.li_div_left.setFrameShape(QFrame.Shape.VLine)
        self.li_div_left.setFrameShadow(QFrame.Shadow.Sunken)
        self.pbtn_add_file = QPushButton(vdi)
        self.pbtn_add_file.setObjectName(u"pbtn_add_file")
        self.pbtn_add_file.setEnabled(False)
        self.pbtn_add_file.setGeometry(QRect(180, 430, 131, 23))
        self.pbtn_add_folder = QPushButton(vdi)
        self.pbtn_add_folder.setObjectName(u"pbtn_add_folder")
        self.pbtn_add_folder.setEnabled(False)
        self.pbtn_add_folder.setGeometry(QRect(180, 460, 131, 23))
        self.pbtn_del_item = QPushButton(vdi)
        self.pbtn_del_item.setObjectName(u"pbtn_del_item")
        self.pbtn_del_item.setEnabled(False)
        self.pbtn_del_item.setGeometry(QRect(320, 430, 131, 23))
        self.pbtn_del_all_changes = QPushButton(vdi)
        self.pbtn_del_all_changes.setObjectName(u"pbtn_del_all_changes")
        self.pbtn_del_all_changes.setEnabled(False)
        self.pbtn_del_all_changes.setGeometry(QRect(320, 460, 131, 23))
        self.li_div_middle = QFrame(vdi)
        self.li_div_middle.setObjectName(u"li_div_middle")
        self.li_div_middle.setGeometry(QRect(450, 430, 41, 51))
        self.li_div_middle.setFrameShape(QFrame.Shape.VLine)
        self.li_div_middle.setFrameShadow(QFrame.Shadow.Sunken)
        self.pbtn_save_file = QPushButton(vdi)
        self.pbtn_save_file.setObjectName(u"pbtn_save_file")
        self.pbtn_save_file.setEnabled(False)
        self.pbtn_save_file.setGeometry(QRect(490, 430, 131, 23))
        self.pbtn_quit = QPushButton(vdi)
        self.pbtn_quit.setObjectName(u"pbtn_quit")
        self.pbtn_quit.setEnabled(False)
        self.pbtn_quit.setGeometry(QRect(490, 460, 131, 23))
        self.li_div_right = QFrame(vdi)
        self.li_div_right.setObjectName(u"li_div_right")
        self.li_div_right.setGeometry(QRect(620, 430, 41, 51))
        self.li_div_right.setFrameShape(QFrame.Shape.VLine)
        self.li_div_right.setFrameShadow(QFrame.Shadow.Sunken)
        self.pbtn_vdi = QPushButton(vdi)
        self.pbtn_vdi.setObjectName(u"pbtn_vdi")
        self.pbtn_vdi.setEnabled(False)
        self.pbtn_vdi.setGeometry(QRect(660, 430, 131, 23))
        self.lb_version_num = QLabel(vdi)
        self.lb_version_num.setObjectName(u"lb_version_num")
        self.lb_version_num.setGeometry(QRect(660, 460, 131, 21))

        self.retranslateUi(vdi)

        QMetaObject.connectSlotsByName(vdi)
    # setupUi

    def retranslateUi(self, vdi):
        vdi.setWindowTitle(QCoreApplication.translate("vdi", u"SAC-VDI\u5b8c\u6574\u6027\u6821\u9a8c\u8c03\u8bd5\u5de5\u5177", None))
        self.lb_base_path.setText(QCoreApplication.translate("vdi", u"\u6821\u9a8c\u6839\u76ee\u5f55 : \u7b49\u5f85\u8bfb\u53d6", None))
        self.pbtn_read_base_path.setText(QCoreApplication.translate("vdi", u"\u8bfb\u53d6VDI\u6839\u76ee\u5f55", None))
        self.pbtn_read_vdi_file.setText(QCoreApplication.translate("vdi", u"\u8bfb\u53d6VDI\u6821\u9a8c\u76ee\u5f55", None))
        self.pbtn_add_file.setText(QCoreApplication.translate("vdi", u"\u6dfb\u52a0\u6587\u4ef6", None))
        self.pbtn_add_folder.setText(QCoreApplication.translate("vdi", u"\u6dfb\u52a0\u6587\u4ef6\u5939", None))
        self.pbtn_del_item.setText(QCoreApplication.translate("vdi", u"\u5220\u9664\u9009\u4e2d\u7684\u9879\u76ee", None))
        self.pbtn_del_all_changes.setText(QCoreApplication.translate("vdi", u"\u64a4\u9500\u6240\u6709\u66f4\u6539", None))
        self.pbtn_save_file.setText(QCoreApplication.translate("vdi", u"\u4fdd\u5b58\u6587\u4ef6", None))
        self.pbtn_quit.setText(QCoreApplication.translate("vdi", u"\u9000\u51fa\u7a0b\u5e8f", None))
        self.pbtn_vdi.setText(QCoreApplication.translate("vdi", u"\u6267\u884cVDI\u6821\u9a8c", None))
        self.lb_version_num.setText(QCoreApplication.translate("vdi", u"\u5f53\u524d\u7248\u672c : \u7b49\u5f85\u52a0\u8f7d", None))
    # retranslateUi

