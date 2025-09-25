
import json
import json_fingerprint
from json_fingerprint import hash_functions
import copy

def write_json_file(data : dict , path : str) -> None:

    # 生成指纹
    fingerprint = json_fingerprint.create(
                input=json.dumps(data),
                hash_function=hash_functions.SHA256,
                version=1
            )
    temp_data = copy.deepcopy(data)
    
    temp_data['sac_jfp'] = fingerprint.split('$')[2]

    with open(path , "w", encoding = "utf-8") as f:
        json.dump(temp_data , f , ensure_ascii = False)
        f.close()
        