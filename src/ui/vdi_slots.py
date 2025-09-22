
from utils.response.vdi_responses import *
from functools import partial
def vdi_slots(self):
    self.pbtn_read_base_path.clicked.connect(partial(res_pbtn_read_base_path , self))