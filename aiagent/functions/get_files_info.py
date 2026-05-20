import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_wd = os.path.abspath(working_directory)
        abs_dir = os.path.normpath(os.path.join(abs_wd, directory))
        is_valid_target = os.path.commonpath([abs_wd, abs_dir]) == abs_wd
    except Exception as e:
        return f'Error: {e}'

    if not is_valid_target:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(abs_dir):
        return f'Error: "{directory}" is not a directory'

    return f'Success: "{directory}" is within the working directory'
