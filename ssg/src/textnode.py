from enum import Enum
from types import NotImplementedType
from typing import Optional

from leafnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode():
    def __init__(
            self,
            text: str,
            text_type: TextType,
            url: Optional[str] = None,
    ) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, TextNode):
            return NotImplemented
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    def __repr__(self) -> str:
        return (
            f"TextNode(text={self.text}, value={self.text_type.value}, url={self.url})"
        )


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            assert text_node.url is not None
            return LeafNode("a", text_node.text, {
                "href": text_node.url,
            })
        case TextType.IMAGE:
            assert text_node.url is not None
            assert text_node.text is not None
            return LeafNode("img", "", {
                "src": text_node.url,
                "alt": text_node.text,
            })
