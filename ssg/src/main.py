from pathlib import Path

from .clone_folder import clone_folder
from .generate_page import generate_page


def main() -> None:
    clone_folder("static", "public")
    generate_page(
        Path("content/index.md"), 
        Path("template.html"), 
        Path("public/index.html")
    )


if __name__ == "__main__":
    main()
