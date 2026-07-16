from textnode import TextNode, TextType


def split_nodes_delimiter(
        old_nodes: list[TextNode],
        delimiter: str,
        text_type: TextType,
 ) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        # Split the node's text
        text = node.text
        while len(text) > 0:
            # Look for first pair of matched delimiters.
            splits = text.split(delimiter, maxsplit=2)
            match len(splits):
                case 1:
                    # Delimiter not found, add new node with text and exit loop
                    new_nodes.append(TextNode(text, TextType.TEXT))
                    break
                case 3:
                    # Pair of delimiters found. Add first as new normal text node if
                    # non-empty.
                    if len(splits[0]) > 0:
                        new_nodes.append(TextNode(splits[0], TextType.TEXT))

                    # Add second as provided text_type node.
                    new_nodes.append(TextNode(splits[1], text_type))

                    # Reduce text and loop if rest is non-empty.
                    text = splits[2]
                case _:
                    raise ValueError(f"Unmatched delimiter {delimiter} in {node.text}")
        
    return new_nodes
