import unittest

from .leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_constructor(self) -> None:
        tag = "TAG"
        value = "VALUE"
        props = {"PROP1": "VAL1", "PROP2": "VAL2"}
        node = LeafNode(tag=tag, value=value, props=props)
        self.assertEqual(node.tag, tag)
        self.assertEqual(node.value, value)
        self.assertIsNone(node.children)
        self.assertEqual(node.props, props)

    def test_leaf_to_html_p(self) -> None:
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self) -> None:
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_value_missing(self) -> None:
        node = LeafNode("p", None) # type: ignore
        self.assertRaises(ValueError, node.to_html)


if __name__ == "__main__":
    unittest.main()
