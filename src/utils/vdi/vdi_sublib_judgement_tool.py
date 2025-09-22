import os

def is_subdirectory(child_path : str , parent_path : str ) -> bool:
    # 获取相对路径
    try:
        relative_path = os.path.relpath(child_path , parent_path)
        # 判断相对路径是否有效
        return not relative_path.startswith('..') and not os.path.isabs(relative_path)
    except ValueError:
        return False