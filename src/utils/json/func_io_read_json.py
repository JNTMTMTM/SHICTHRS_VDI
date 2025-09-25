
import json
import copy
from typing import Union
from utils.json.func_io_json_jfp_verify import verify_json_file

def read_json_file(path : str) -> Union[dict , bool]:
    with open(path , "r" , encoding = "utf-8") as f:
        data = json.load(f)
        f.close()
        
    tempdict : dict = copy.deepcopy(data) 

    if verify_json_file(tempdict):
        return tempdict
    else:
        return None
    