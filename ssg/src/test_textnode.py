import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self) -> None:
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq_text(self) -> None:
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a test node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_neq_type(self) -> None:
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    def test_url_omitted(self) -> None:
        node = TextNode("This is a text node", TextType.PLAIN)
        self.assertIsNone(node.url)

    def test_url_specified(self) -> None:
        node = TextNode("This is a text node", TextType.PLAIN, "https://www.boot.dev")
        self.assertEqual(node.url, "https://www.boot.dev")

    def test_eq_with_url(self) -> None:
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_neq_url(self) -> None:
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
