from extract_markdown import extract_markdown_images, extract_markdown_links
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

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        # Find the images
        text = node.text
        images = extract_markdown_images(text)

        # Create the image nodes and add surrounding text as plain text nodes. 
        for image in images:
            # Split the text around the specified image
            splits = text.split(f"![{image[0]}]({image[1]})", maxsplit=1)

            # There should always be exactly 2 elements in splits.
            assert len(splits) == 2, f"Could not find image in text?!? {text}"

            # Add the first split as a plain text node if non-empty.
            if len(splits[0]) > 0:
                new_nodes.append(TextNode(splits[0], TextType.TEXT))

            # Add the image node.
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))

            # Reduce text and loop if rest is non-empty.
            text = splits[1]
        
        # Add the remaining text as a plain text node if not empty.
        if len(text) > 0:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        # Find the links
        text = node.text
        links = extract_markdown_links(text)

        # Create the link nodes and add surrounding text as plain text nodes. 
        for link in links:
            # Split the text around the specified link
            splits = text.split(f"[{link[0]}]({link[1]})", maxsplit=1)

            # There should always be exactly 2 elements in splits.
            assert len(splits) == 2, f"Could not find link in text?!? {text}"

            # Add the first split as a plain text node if non-empty.
            if len(splits[0]) > 0:
                new_nodes.append(TextNode(splits[0], TextType.TEXT))

            # Add the link node.
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))

            # Reduce text and loop if rest is non-empty.
            text = splits[1]
        
        # Add the remaining text as a plain text node if not empty.
        if len(text) > 0:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes
