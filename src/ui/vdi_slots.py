
from utils.response.vdi_responses import *
from functools import partial

def vdi_slots(self , var):
    self.pbtn_read_base_path.clicked.connect(partial(res_pbtn_read_base_path , self , var))  # 读取VDI根目录
    self.pbtn_read_vdi_file.clicked.connect(partial(res_pbtn_read_vdi_file , self , var))  # 读取VDI校验目录文件
    self.pbtn_add_file.clicked.connect(partial(res_pbtn_add_file , self , var))  # 添加文件
    self.pbtn_add_folder.clicked.connect(partial(res_pbtn_add_folder , self , var))  # 添加文件夹
    self.pbtn_del_item.clicked.connect(partial(res_pbtn_del_item , self , var))  # 删除选中项
    self.pbtn_del_all_changes.clicked.connect(partial(res_pbtn_del_all_changes , self , var))  # 删除所有修改