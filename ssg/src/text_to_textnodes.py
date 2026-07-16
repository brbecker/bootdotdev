from .split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from .textnode import TextNode, TextType


def text_to_textnodes(text: str) -> list[TextNode]:
    # Create initial list of TextNodes
    nodes = [TextNode(text, TextType.TEXT)]

    # There should be no nested Markdown tabs, so just apply the splitters in sequence.
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    # Return list of nodes
    return nodes
