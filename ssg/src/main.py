# from pathlib import Path

from .clone_folder import clone_folder
# from .textnode import TextNode, TextType


def main() -> None:
    # node = TextNode(
    #     "This is some anchor text",
    #     TextType.LINK,
    #     "https://www.boot.dev",
    #     )
    # print(node)
    clone_folder("static", "public")

if __name__ == "__main__":
    main()
