def markdown_to_blocks(md: str) -> list[str]:
    blocks = md.split("\n\n")
    blocks = map(lambda s: s.strip(), blocks)
    blocks = filter(lambda s: s != "", blocks)
    return list(blocks)
