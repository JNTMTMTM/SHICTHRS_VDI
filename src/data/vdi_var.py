
import os

class vdi_var():
    def __init__(self):
        self.EXEPATH : str = os.getcwd()  # 获取当前执行程序的路径
        self.VDI_BASEPATH : str = ''  # VDI根目录
        self.VDI_FILEPATH : str = ''  # VDI校验项目目录路径
        self.VDI_ORG_FILEDATA : dict = {}  # VDI校验项目目录元数据
        self.VDI_CHANGED_FILEDATA : dict = {}  # VDI校验项目目录修改数据
        self.VDI_LVHEADERS : list = ['文件名' , '类型' , '路径']