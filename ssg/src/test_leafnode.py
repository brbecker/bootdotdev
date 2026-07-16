import unittest
from leafnode import LeafNode


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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_value_missing(self):
        node = LeafNode("p", None) # type: ignore
        self.assertRaises(ValueError, node.to_html)


    # def test_html_noprops(self) -> None:
    #     node = HTMLNode()
    #     self.assertEqual(node.props_to_html(), "")

    # def test_html_props(self) -> None:
    #     node = HTMLNode(props={"PROP1": "VAL1", "PROP2": "VAL2"})
    #     html = node.props_to_html()
    #     # Order of the props is not relevant
    #     self.assertTrue(' PROP1="VAL1"' in html)
    #     self.assertTrue(' PROP2="VAL2"' in html)

    # def test_eq(self) -> None:
    #     tag = "TAG"
    #     value = "VALUE"
    #     children = ["CHILD1", "CHILD2"]
    #     props = {"PROP1": "VAL1", "PROP2": "VAL2"}
    #     node1 = HTMLNode(tag=tag, value=value, children=children, props=props)
    #     node2 = HTMLNode(tag=tag, value=value, children=children, props=props)
    #     self.assertEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
