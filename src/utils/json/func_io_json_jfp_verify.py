import json
import json_fingerprint
from json_fingerprint import hash_functions

def verify_json_file(pre_verfiy_dict : dict) -> bool:
    jsp = None

    # 加载json指纹
    jsp = pre_verfiy_dict['sac_jfp']

    # 删除json指纹
    del pre_verfiy_dict['sac_jfp']

    fingerprint = json_fingerprint.create(
                input=json.dumps(pre_verfiy_dict),
                hash_function=hash_functions.SHA256,
                version=1
            )

    if jsp == fingerprint.split('$')[2]:
        return True
    else:
        return False