import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_parent_no_tag(self) -> None:
        child_node = LeafNode(tag="p", value="value")
        parent_node = ParentNode(tag=None, children=[child_node]) # type: ignore
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_parent_no_children(self) -> None:
        parent_node = ParentNode(tag="p", children=None) # type: ignore
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_with_children(self) -> None:
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self) -> None:
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_zero_children(self) -> None:
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_many_children(self) -> None:
        child1_node = LeafNode("span", "child1")
        child2_node = LeafNode("p", "child2")
        child3_node = LeafNode("b", "child3")
        parent_node = ParentNode("div", [child1_node, child2_node, child3_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child1</span><p>child2</p><b>child3</b></div>",
        )

    def test_to_html_zero_grandchildren(self) -> None:
        child_node = ParentNode("span", [])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span></span></div>")

    def test_to_html_many_grandchildren(self) -> None:
        grandchild1_node = LeafNode("b", "grandchild1")
        grandchild2_node = LeafNode("i", "grandchild2")
        grandchild3_node = LeafNode("b", "grandchild3")
        child_node = ParentNode("span", [
            grandchild1_node, grandchild2_node, grandchild3_node
        ])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild1</b><i>grandchild2</i><b>grandchild3</b></span>"
            "</div>",
        )
