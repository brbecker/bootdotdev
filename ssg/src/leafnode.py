from typing import Optional

from .htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
            self,
            tag: str | None,
            value: str,
            props: Optional[dict[str, str]] = None,
    ) -> None:
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError('All leaf nodes must have a value.')
        
        if self.tag is None:
            # Value is raw text
            return self.value
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self) -> str:
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"
