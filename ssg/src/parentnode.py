from typing import Optional

from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
            self,
            tag: str,
            children: list["HTMLNode"],
            props: Optional[dict[str, str]] = None,
    ) -> None:
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self) -> str | ValueError:
        if self.tag is None:
            raise ValueError('All parent nodes must have a tag.')

        if self.children is None:
            raise ValueError('All parent nodes must have a list of 0 or more children.')

        retval = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            retval += str(child.to_html())
        retval += f'</{self.tag}>'

        return retval

    def __repr__(self) -> str:
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"
