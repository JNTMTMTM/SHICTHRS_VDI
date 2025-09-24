
from PySide6.QtWidgets import QTableWidgetItem , QMessageBox
from PySide6.QtGui import QColor
import os 

def update_vdi_list(self , var):
    try:
        self.tw_main.clearContents()  # 清空表格内容
        self.tw_main.setRowCount(0)  # 设置列数
        self.tw_main.resizeColumnsToContents()
        if var.VDI_CHANGED_FILEDATA['vdi_table'].keys():
            self.tw_main.setRowCount(len(var.VDI_CHANGED_FILEDATA['vdi_table'].keys()))  # 设置行数
            current_row : int = 0  # 初始化行数索引
            for vdi_index in var.VDI_CHANGED_FILEDATA['vdi_table'].keys():
                count_column : int  = 0  # 初始化列数索引
                for vdi_item in var.VDI_CHANGED_FILEDATA['vdi_table'][vdi_index].keys():
                    if vdi_item == 'path':
                        temp_item : QTableWidgetItem = QTableWidgetItem(os.path.join(var.VDI_BASEPATH , *var.VDI_CHANGED_FILEDATA['vdi_table'][vdi_index][vdi_item]))
                    elif vdi_item == 'type':
                        temp_item : QTableWidgetItem = QTableWidgetItem(var.VDI_CHANGED_FILEDATA['vdi_table'][vdi_index][vdi_item])
                        # 根据类型设置背景颜色
                        if var.VDI_CHANGED_FILEDATA['vdi_table'][vdi_index][vdi_item] == 'folder':
                            temp_item.setBackground(QColor(0 , 255 , 0 , 32))
                            
                        elif var.VDI_CHANGED_FILEDATA['vdi_table'][vdi_index][vdi_item] == 'file':
                            temp_item.setBackground(QColor(255 , 0 , 0 , 32))
                    else:
                        temp_item : QTableWidgetItem = QTableWidgetItem(var.VDI_CHANGED_FILEDATA['vdi_table'][vdi_index][vdi_item])

                    self.tw_main.setItem(current_row , count_column , temp_item)
                    count_column += 1
                current_row += 1

            del current_row , count_column  # 删除临时变量
            self.tw_main.resizeColumnsToContents()
    except Exception as e:
        QMessageBox.critical(self , "SAC_VDI" , f"更新VDI列表失败 : {e}")