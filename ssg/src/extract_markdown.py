import re


extract_markdown_images_re = r"!\[(.*?)\]\((.*?)\)"
extract_markdown_links_re = r"(?<!!)\[(.*?)\]\((.*?)\)"

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(extract_markdown_images_re, text)

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(extract_markdown_links_re, text)
