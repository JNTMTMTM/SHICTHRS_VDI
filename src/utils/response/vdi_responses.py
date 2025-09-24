
from PySide6.QtWidgets import QFileDialog , QMessageBox
from utils.vdi.vdi_sublib_judgement_tool import is_subdirectory
from utils.json.func_io_read_json import read_json_file
from utils.vdi.vdi_update_vdilist import update_vdi_list
from copy import deepcopy
import os




# 响应 pbtn_read_base_path 读取VDI根目录
def res_pbtn_read_base_path(self , var) -> None:
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

                # 选择VDI校验目录后终止激活控件
                self.tw_main.clearContents()  # 清空表格内容
                self.tw_main.setRowCount(0)  # 设置列数
                self.tw_main.resizeColumnsToContents()  # 调整列宽
                self.pbtn_add_file.setEnabled(False)
                self.pbtn_add_folder.setEnabled(False)
                self.pbtn_del_item.setEnabled(False)
                self.pbtn_del_all_changes.setEnabled(False)
                self.pbtn_save_file.setEnabled(False)
                self.pbtn_vdi.setEnabled(False)
                
            else:
                QMessageBox.warning(self , "SAC_VDI" , "文件夹不存在")
        else:
            QMessageBox.warning(self , "SAC_VDI" , "未选择文件夹")
    except Exception as e:
        QMessageBox.critical(self , "SAC_VDI" , f"读取VDI根目录失败 : {e}")

# 响应 pbtn_read_vdi_file 读取VDI校验目录文件
def res_pbtn_read_vdi_file(self , var) -> None:
    try:
        temp_file_path , _ = QFileDialog.getOpenFileName(self , "选择VDI校验目录文件" , "" , "JSON File (*.json)")
        if temp_file_path:  # 如果选择了文件
            if os.path.exists(temp_file_path):
                var.VDI_FILEPATH = deepcopy(temp_file_path)  # 将文件路径保存到全局变量中
                del temp_file_path  # 删除临时路径

                # 判断是否在根目录下
                if is_subdirectory(var.VDI_FILEPATH , var.VDI_BASEPATH):

                    # 判断是否为vdi检查目录
                    if os.path.basename(var.VDI_FILEPATH) == 'sac_vdi.json':
                        QMessageBox.information(self , "SAC_VDI" , "读取VDI校验目录文件成功")
                        # 激活控件
                        self.tw_main.clearContents()  # 清空表格内容
                        self.tw_main.setRowCount(0)  # 设置列数
                        self.tw_main.resizeColumnsToContents()  # 调整列宽
                        self.pbtn_add_file.setEnabled(True)
                        self.pbtn_add_folder.setEnabled(True)
                        self.pbtn_del_item.setEnabled(True)
                        self.pbtn_del_all_changes.setEnabled(True)
                        self.pbtn_save_file.setEnabled(True)
                        self.pbtn_vdi.setEnabled(True)

                        # 对vdi校验目录处理
                        var.VDI_ORG_FILEDATA = deepcopy(list(read_json_file(var.VDI_FILEPATH)['vdi_table'].values()))  # 读取原始文件数据
                        var.VDI_CHANGED_FILEDATA = deepcopy(var.VDI_ORG_FILEDATA)  # 拷贝临时修改数据

                        # 判断是否有vdi_table
                        update_vdi_list(self , var)  # 更新列表

                    else:
                        QMessageBox.warning(self , "SAC_VDI" , "文件不是VDI校验目录文件")
                else:
                    var.VDI_FILEPATH : str = ''
                    QMessageBox.warning(self , "SAC_VDI" , "文件不在VDI根目录下")
            else:
                QMessageBox.warning(self , "SAC_VDI" , "文件不存在")
        else:
            QMessageBox.warning(self , "SAC_VDI" , "未选择文件")
    except Exception as e:
        QMessageBox.critical(self , "SAC_VDI" , f"读取VDI校验目录文件失败 : {e}")   

# 响应 pbtn_add_file 添加文件
def res_pbtn_add_file(self , var) -> None:
    try:
        back_up_VDI_CHANGED_FILEDATA : list = deepcopy(var.VDI_CHANGED_FILEDATA)  # 备份修改数据
        temp_file_path , _ = QFileDialog.getOpenFileName(self , "添加文件至VDI校验目录" , "" , "ALL FILES (*.*)")
        if temp_file_path:  # 如果选择了文件
            temp_file_path = temp_file_path.replace(var.VDI_BASEPATH , '')  # 替换根目录

            var.VDI_CHANGED_FILEDATA.append({
                "name": os.path.basename(temp_file_path),
                "type": "file",
                "path": temp_file_path.split('/')[1:]
            },)

            update_vdi_list(self , var)
        else:
            QMessageBox.warning(self , "SAC_VDI" , "未选择文件")

    except Exception as e:
        var.VDI_CHANGED_FILEDATA = deepcopy(back_up_VDI_CHANGED_FILEDATA)  # 恢复修改数据
        update_vdi_list(self , var)
        QMessageBox.critical(self , "SAC_VDI" , f"添加文件至VDI校验目录失败 : {e}")


