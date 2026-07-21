from genericpath import isdir, isfile
import os
import os.path

from .generate_page import generate_page


def generate_pages_recursively(
    dir_path_content: str,
    template_path: str,
    dest_dir_path: str,
):
    if not os.path.exists(dest_dir_path):
        print(f"Creating directory {dest_dir_path}")
        os.mkdir(dest_dir_path)

    for e in os.listdir(dir_path_content):
        src = os.path.join(dir_path_content, e)
        dst = os.path.join(dest_dir_path, e)
        print(f"Processing entry {src}")
        if os.path.isfile(src):
            if src.endswith(".md"):
                dst = os.path.join(dest_dir_path, e.replace(".md", ".html"))
                generate_page(src, template_path, dst)
            else:
                print(f"{src} not a Markdown file, skipping")
        elif os.path.isdir(src):
            dst = os.path.join(dest_dir_path, e)
            generate_pages_recursively(src, template_path, dst)
