from enum import Enum
from types import NotImplementedType
from typing import Optional


class TextType(Enum):
    PLAIN = "plain"
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
