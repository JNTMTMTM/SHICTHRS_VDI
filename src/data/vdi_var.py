
import os

class vdi_var():
    def __init__(self):
        self.VDI_VERSION : str = '0.0.1'  # VDI版本
        self.EXEPATH : str = os.getcwd()  # 获取当前执行程序的路径
        self.VDI_BASEPATH : str = ''  # VDI根目录
        self.VDI_FILEPATH : str = ''  # VDI校验项目目录路径
        self.VDI_ORG_FILEDATA : list = {}  # VDI校验项目目录元数据
        self.VDI_CHANGED_FILEDATA : list = {}  # VDI校验项目目录修改数据
        self.VDI_LVHEADERS : list = ['文件名' , '类型' , '路径']