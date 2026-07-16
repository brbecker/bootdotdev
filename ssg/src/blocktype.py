import re

from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block: str) -> BlockType:
    # Heading
    if re.match(r"#{1,6} ", block):
        return BlockType.HEADING
    
    # Code
    if block.startswith("```\n") and block.endswith("\n```"):
        return BlockType.CODE

    # Remaining tests look at each line.
    blocklines = block.split("\n")

    # Quote block: Each line starts with re "> ?"
    for line in blocklines:
        if not re.match("> ?", line):
            break
    else: # for loop, if break not hit
        return BlockType.QUOTE

    # Unordered list: Each line starts with "- "
    for line in blocklines:
        if not line.startswith("- "):
            break
    else: # for loop, if break not hit
        return BlockType.UNORDERED_LIST

    # Ordered list: Each line starts with "#. ", where # starts at 1 and increments by 1
    counter = 1
    for line in blocklines:
        if not line.startswith(f"{counter}. "):
            break
        counter += 1
    else: # for loop, if break not hit
        return BlockType.ORDERED_LIST
    
    # Nothing matched
    return BlockType.PARAGRAPH
