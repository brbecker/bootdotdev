import os
import os.path
import shutil


def copy_directory(source: str, target: str) -> None:
    if os.path.exists(target):
        print(f"Directory {target} already existed.")
    else:
        print(f"Creating directory {target}")
        os.mkdir(target)

    for e in os.listdir(source):
        entry = os.path.join(source, e)
        print(f"Processing entry {entry} ...")
        if os.path.isfile(entry):
            print(f"Copying file {entry} to {target}")
            shutil.copy(entry, target)
        elif os.path.isdir(entry):
            tgt_path = os.path.join(target, e)
            copy_directory(entry, tgt_path)


def clone_folder(source: str, target: str) -> None:
    # Clear out the target folder
    if os.path.exists(target):
        print(f"Clearing directory {target}")
        shutil.rmtree(target)

    copy_directory(source, target)
