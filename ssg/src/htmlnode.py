from types import NotImplementedType
from typing import Optional


class HTMLNode():
    def __init__(
            self,
            tag: Optional[str] = None,
            value: Optional[str] = None,
            children: Optional[list["HTMLNode"]] = None,
            props: Optional[dict[str, str]] = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str | NotImplementedError | ValueError:
        raise NotImplementedError()
    
    def props_to_html(self) -> str:
        if self.props is None:
            return ""

        retval = ""
        for prop, value in self.props.items():
            retval += f' {prop}="{value}"'
        return retval

    def __eq__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, HTMLNode):
            return NotImplemented
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )

    def __repr__(self) -> str:
        return (
            f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, "
            f"props={self.props})"
        )
