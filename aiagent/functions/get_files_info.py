import os

from google.genai import types


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

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

    # Valid directory, process the files
    # return f'Success: "{directory}" is within the working directory'
    file_data: list[str] = []
    try:
        for filename in os.listdir(abs_dir):
            # print(f"filename is {filename}")
            abs_filename = os.path.join(abs_dir, filename)
            # print(f"abs_filename is {abs_filename}")
            file_size = os.path.getsize(abs_filename)
            is_dir = os.path.isdir(abs_filename)
            file_data.append(f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}")
    except Exception as e:
        print(f"Error: {e}")

    return "\n".join(file_data)
