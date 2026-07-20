from pathlib import Path

from .extract_title import extract_title

from .markdown_to_htmlnode import markdown_to_html_node


def generate_page(
    from_path: Path,
    template_path: Path,
    dest_path: Path
) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        from_markdown = f.read()
    with open(template_path, "r") as f:
        template_contents = f.read()
    
    from_html = markdown_to_html_node(from_markdown).to_html()
    title = extract_title(from_markdown)

    final_html = template_contents \
        .replace("{{ Title }}", title) \
        .replace("{{ Content }}", from_html)

    with open(dest_path, "w") as f:
        f.write(final_html)
