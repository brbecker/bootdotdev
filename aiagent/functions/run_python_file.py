import os
import subprocess

from google.genai import types


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a specified Python script located in a specified directory relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path of the Python script to run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional list of arguments to the Python function",
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Argument to the python script",
                ),
            )
        },
        required=["file_path"],
    ),
)

def run_python_file(
        working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        abs_wd = os.path.abspath(working_directory)
        abs_fp = os.path.normpath(os.path.join(abs_wd, file_path))
        is_valid_target = os.path.commonpath([abs_wd, abs_fp]) == abs_wd

        if not is_valid_target:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_fp):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", abs_fp]
        if args:
            command.extend(args)
        completed_process = subprocess.run(
            command,
            capture_output=True,
            cwd=os.path.dirname(abs_fp),
            text=True,
            timeout=30,
        )

    except Exception as e:
        return f"Error: executing Python file: {e}"

    outputs = []
    if completed_process.returncode != 0:
        outputs.append(f"Process exited with code {completed_process.returncode}")
    if not completed_process.stdout and not completed_process.stderr:
        outputs.append("No output produced")
    else:
        outputs.append(f"STDOUT: {completed_process.stdout}")
        outputs.append(f"STDERR: {completed_process.stderr}")

    return "; ".join(outputs)
