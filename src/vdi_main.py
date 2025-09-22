
# # -*- coding: utf-8 -*-

# SHICTHRS VDI
# 立项时间 20250922
# 开发人员 : 鸡哥

# © 2025-2026 SHICTHRS, Std. All rights reserved.

# 算法诠释一切 质疑即是认可
# Algorithms = rule ; Questioning = approval

import sys , os
sys.path.append("..")

from PySide6.QtWidgets import (QApplication , QMainWindow)
from PySide6 import QtGui , QtWidgets
from ui.vdi_ui import Ui_vdi

class vdi_gui(Ui_vdi , QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(os.getcwd() , 'icon' , 'logo_32x32.ico')))
    app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    vdi_gui = vdi_gui()
    sys.exit(app.exec())