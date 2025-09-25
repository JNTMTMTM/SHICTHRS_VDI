
def format_vdi_tabel(vdi_tabel : list) -> dict:
    temp_reutrn_dict : dict = {'vdi_table' : {}}  # 临时返回字典
    temp_index : int = 1  # 临时索引

    for vdi_index in vdi_tabel:
        temp_reutrn_dict['vdi_table'][temp_index] = vdi_index
        temp_index += 1

    return temp_reutrn_dict