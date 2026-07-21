from .clone_folder import clone_folder
from .generate_pages_recursively import generate_pages_recursively


def main() -> None:
    clone_folder("static", "public")
    generate_pages_recursively(
        "content",
        "template.html",
        "public",
    )


if __name__ == "__main__":
    main()
