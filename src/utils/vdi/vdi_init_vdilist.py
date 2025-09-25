
from PySide6.QtWidgets import QTableWidget

def init_vdi_list(self , var):
    self.tw_main.setColumnCount(len(var.VDI_LVHEADERS))
    self.tw_main.setHorizontalHeaderLabels(var.VDI_LVHEADERS)

    header_level_1 = self.tw_main.horizontalHeader()
    header_level_1.setMinimumSectionSize(100)

    self.tw_main.setEditTriggers(QTableWidget.NoEditTriggers)
    self.tw_main.setSelectionMode(QTableWidget.SingleSelection)