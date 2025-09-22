
import json
import copy

from func_io_json_jfp_verify import verify_json_file

def read_json_file(qmb , path : str) ->dict:
    with open(path , "r" , encoding = "utf-8") as f:
        data = json.load(f)
        f.close()
        
    tempdict : dict = copy.deepcopy(data) 

    if verify_json_file(tempdict):
        return tempdict
    else:
        qmb.generateNormalQMessageBox('CRITICAL' , '' , 'JFP Verification Failed')
        return {}
        return False
    