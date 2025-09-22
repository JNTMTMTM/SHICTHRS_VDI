
# # -*- coding: utf-8 -*-

# SHICTHRS VDI
# 立项时间 20250922
# 开发人员 : 鸡哥

# © 2025-2026 SHICTHRS, Std. All rights reserved.

# 算法诠释一切 质疑即是认可
# Algorithms = rule ; Questioning = approval

import sys
sys.path.append("..")

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTableView, QWidget)
from ui.vdi_ui import Ui_vdi

class vdi_gui(Ui_vdi , QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    vdi_gui = vdi_gui()
    sys.exit(app.exec())