
from PySide6.QtWidgets import QFileDialog , QMessageBox
from copy import deepcopy
import os




# 响应 pbtn_read_base_path 读取VDI根目录
def res_pbtn_read_base_path(self , var):
    try:
        temp_folder_path : str= QFileDialog.getExistingDirectory(self , "选择VDI根目录")
        if temp_folder_path:  # 如果选择了文件夹
            if os.path.exists(temp_folder_path):
                var.VDI_BASEPATH = deepcopy(temp_folder_path)  # 将文件夹路径保存到全局变量中
                del temp_folder_path  # 删除临时路径

                QMessageBox.information(self , "SAC_VDI" , "读取VDI根目录成功")
                self.lb_base_path.setText(f"校验根目录 : {var.VDI_BASEPATH}")

                # 选择VDI校验目录控件
                self.pbtn_read_vdi_file.setEnabled(True)
                # self.pbtn_add_file.setEnabled(True)
                # self.pbtn_add_folder.setEnabled(True)
                # self.pbtn_del_item.setEnabled(True)
                # self.pbtn_del_all_changes.setEnabled(True)
                # self.pbtn_save_file.setEnabled(True)
                # self.pbtn_vdi.setEnabled(True)
            else:
                QMessageBox.warning(self , "SAC_VDI" , "文件夹不存在")
        else:
            QMessageBox.warning(self , "SAC_VDI" , "未选择文件夹")
    except Exception as e:
        QMessageBox.critical(self , "SAC_VDI" , f"读取VDI根目录失败 : {e}")



