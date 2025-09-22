
from utils.response.vdi_responses import *
from functools import partial

def vdi_slots(self , var):
    self.pbtn_read_base_path.clicked.connect(partial(res_pbtn_read_base_path , self , var))  # 读取VDI根目录
    self.pbtn_read_vdi_file.clicked.connect(partial(res_pbtn_read_vdi_file , self , var))  # 读取VDI校验目录文件