import re

from typing import Callable

from .blocktype import BlockType, block_to_block_type
from .htmlnode import HTMLNode
from .leafnode import LeafNode
from .markdown_to_blocks import markdown_to_blocks
from .parentnode import ParentNode
from .text_to_textnodes import text_to_textnodes
from .textnode import text_node_to_html_node


def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(text.replace("\n", " "))
    return list(map(text_node_to_html_node, text_nodes))

def markdown_block_to_paragraph_node(block: str)  -> HTMLNode:
    return ParentNode("p", text_to_children(block))

def markdown_block_to_heading_node(block: str)  -> HTMLNode:
    # Heading must match "#{1,6} ". Split on the space.
    heading_type, heading = block.split(" ", maxsplit=1)
    return ParentNode(
        f"h{len(heading_type)}",
        text_to_children(heading),
    )

def markdown_block_to_code_node(block: str)  -> HTMLNode:
    # Strip code delimiters (initial ```\n and final ```). Do not process internal text.
    # Return "code" node inside "pre" node.
    return ParentNode(
        "pre", [
            LeafNode("code", block[4:-3])
        ]
    )

def markdown_block_to_quote_node(block: str)  -> HTMLNode:
    # Split the block into lines, strip off the leading RE "> ?", and rejoin with
    # spaces.
    blocklines = block.split("\n")
    stripped_lines =  map(lambda s: re.sub(r'^> ?', '', s), blocklines)
    joined = " ".join(stripped_lines)
    return ParentNode("blockquote", text_to_children(joined))

def markdown_list_items(delimiter: str, block: str) -> list[HTMLNode]:
    nodes = []

    # Split the block at the delimiters.
    items = re.split(delimiter, block)

    # First item is guaranteed to be empty string. Ignore it.
    for item in items[1:]:
        nodes.append(
            ParentNode("li", text_to_children(item))
        )

    return nodes

def markdown_block_to_unordered_node(block: str)  -> HTMLNode:
    return ParentNode("ul", markdown_list_items(r"(?m)\n?^- ", block))

def markdown_block_to_ordered_node(block: str)  -> HTMLNode:
    return ParentNode("ol", markdown_list_items(r"(?m)\n?^\d+. ", block))

def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)

    block_converter: dict[BlockType, Callable[[str], HTMLNode]] = {
        BlockType.PARAGRAPH: markdown_block_to_paragraph_node,
        BlockType.HEADING: markdown_block_to_heading_node,
        BlockType.CODE: markdown_block_to_code_node,
        BlockType.QUOTE: markdown_block_to_quote_node,
        BlockType.UNORDERED_LIST: markdown_block_to_unordered_node,
        BlockType.ORDERED_LIST: markdown_block_to_ordered_node,
    }

    nodes: list[HTMLNode] = []
    for block in blocks:
        # Get the type of the block
        block_type = block_to_block_type(block)

        # Convert block to HTMLNode
        node = block_converter[block_type](block)

        # Add node to list
        nodes.append(node)

    return ParentNode("div", nodes)
