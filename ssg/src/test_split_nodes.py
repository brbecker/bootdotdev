import unittest

from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and "
            "another ![second image](https://i.imgur.com/3elNhQu.png).",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(".", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images_not_text(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and "
            "another ![second image](https://i.imgur.com/3elNhQu.png).",
            TextType.BOLD,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)

    def test_split_images_just_image(self):
        node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")],
            new_nodes
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and "
            "another [second link](https://i.imgur.com/3elNhQu.png).",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(".", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links_not_text(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and "
            "another [second link](https://i.imgur.com/3elNhQu.png).",
            TextType.BOLD,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_split_links_just_link(self):
        node = TextNode("[link](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png")],
            new_nodes
        )

    def test_split_images_both(self):
        node = TextNode(
            "This is text with a link [link](https://i.imgur.com/zjjcJKZ.png) and "
            "an image ![image](https://i.imgur.com/3elNhQu.png).",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode(
                    "This is text with a link [link](https://i.imgur.com/zjjcJKZ.png) "
                    "and an image ",
                    TextType.TEXT
                ),
                TextNode(
                    "image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(".", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links_both(self):
        node = TextNode(
            "This is text with a link [link](https://i.imgur.com/zjjcJKZ.png) and "
            "an image ![image](https://i.imgur.com/3elNhQu.png).",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(
                    " and an image ![image](https://i.imgur.com/3elNhQu.png).",
                    TextType.TEXT,
                ),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
