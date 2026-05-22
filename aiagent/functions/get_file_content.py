import os

from google.genai import types

from config import MAX_CHARS


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads the contents of a specified file relative to the working directory, truncated to at most {MAX_CHARS} characters.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to read content from, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_wd = os.path.abspath(working_directory)
        abs_fp = os.path.normpath(os.path.join(abs_wd, file_path))
        is_valid_target = os.path.commonpath([abs_wd, abs_fp]) == abs_wd

        if not is_valid_target:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_fp):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read up to MAX_CHARS from the file
        with open(abs_fp, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            # Did we read the entire file?
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content_string

    except Exception as e:
        return f'Error: {e}'
