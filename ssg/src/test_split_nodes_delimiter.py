import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodeDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_empty_list(self) -> None:
        self.assertListEqual(
            split_nodes_delimiter([], "**", TextType.BOLD),
            [],
        )

    def test_split_nodes_delimiter_empty_text(self) -> None:
        node=TextNode("", TextType.TEXT)
        self.assertListEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD),
            [],
        )

    def test_split_nodes_delimiter_not_text(self) -> None:
        node=TextNode("bolded", TextType.BOLD)
        self.assertListEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD),
            [node],
        )

    def test_split_nodes_delimiter_bold(self) -> None:
        node=TextNode("this is **bolded** text", TextType.TEXT)
        self.assertListEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD),
            [
                TextNode("this is ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
        )

    def test_split_nodes_delimiter_bold_start(self) -> None:
        node=TextNode("**bolded** text", TextType.TEXT)
        self.assertListEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD),
            [
                TextNode("bolded", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
        )

    def test_split_nodes_delimiter_bold_end(self) -> None:
        node=TextNode("this is **bolded**", TextType.TEXT)
        self.assertListEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD),
            [
                TextNode("this is ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
            ],
        )

    def test_split_nodes_delimiter_bold_multiple(self) -> None:
        node=TextNode("this is **bolded** text. And some **more bolded** text.", TextType.TEXT)
        self.assertListEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD),
            [
                TextNode("this is ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" text. And some ", TextType.TEXT),
                TextNode("more bolded", TextType.BOLD),
                TextNode(" text.", TextType.TEXT),
            ],
        )

    def test_split_nodes_delimiter_unbalanced(self) -> None:
        node=TextNode("this is **bolded** text. And some **unbalanced text.", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter(
                [node],
                "**",
                TextType.BOLD,
            )

    def test_split_nodes_delimiter_italic(self) -> None:
        node=TextNode("this is _italic_ text", TextType.TEXT)
        self.assertListEqual(
            split_nodes_delimiter([node], "_", TextType.ITALIC),
            [
                TextNode("this is ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT),
            ],
        )

    def test_split_nodes_delimiter_code(self) -> None:
        node=TextNode("this is `program code` text", TextType.TEXT)
        self.assertListEqual(
            split_nodes_delimiter([node], "`", TextType.CODE),
            [
                TextNode("this is ", TextType.TEXT),
                TextNode("program code", TextType.CODE),
                TextNode(" text", TextType.TEXT),
            ],
        )


if __name__ == "__main__":
    unittest.main()
