
# # -*- coding: utf-8 -*-

# SHICTHRS VDI
# 立项时间 20250922
# 开发人员 : 鸡哥

# © 2025-2026 SHICTHRS, Std. All rights reserved.

# 算法诠释一切 质疑即是认可
# Algorithms = rule ; Questioning = approval

import sys , os
sys.path.append("..")

from PySide6.QtWidgets import QApplication , QMainWindow , QFileDialog
from PySide6 import QtGui , QtWidgets
from ui.vdi_ui import Ui_vdi
from ui.vdi_slots import vdi_slots
from data.vdi_var import vdi_var

class vdi_gui(Ui_vdi , QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        vdi_slots(self , var)
        self.show()
    
    
    


if __name__ == "__main__":
    # 激活全局变量
    var = vdi_var()
    
    # 初始化应用程序
    app = QApplication(sys.argv)

    # 设置图标
    app.setWindowIcon(QtGui.QIcon(os.path.join(var.EXEPATH , 'icon' , 'logo_32x32.ico')))

    # 使用fusion主题
    app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    
    # 初始化主窗口
    vdi_gui = vdi_gui()
    
    sys.exit(app.exec())