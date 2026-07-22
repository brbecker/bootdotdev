import sys

from .clone_folder import clone_folder
from .generate_pages_recursively import generate_pages_recursively


def main() -> None:
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    dest_dir = "docs"

    clone_folder("static", dest_dir)
    generate_pages_recursively(
        "content",
        "template.html",
        dest_dir,
        basepath,
    )


if __name__ == "__main__":
    main()
