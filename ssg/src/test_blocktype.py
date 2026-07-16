import unittest

from blocktype import BlockType, block_to_block_type


class TestBlockType(unittest.TestCase):
    def test_block_type_h1(self):
        self.assertEqual(block_to_block_type(r"# H1"), BlockType.HEADING)

    def test_block_type_h3(self):
        self.assertEqual(block_to_block_type(r"### H3"), BlockType.HEADING)

    def test_block_type_h6(self):
        self.assertEqual(block_to_block_type(r"###### H6"), BlockType.HEADING)

    def test_block_type_h7_not_heading(self):
        self.assertEqual(block_to_block_type(r"####### H7"), BlockType.PARAGRAPH)

    def test_block_type_code(self):
        block = """
```
This is code
```
"""
        self.assertEqual(block_to_block_type(block.strip()), BlockType.CODE)

    def test_block_type_not_code(self):
        block = """
```
This is not code. Missing one close backtick. 
``
"""
        self.assertEqual(block_to_block_type(block.strip()), BlockType.PARAGRAPH)

    def test_block_type_quote(self):
        block = """
> This
>is
> a
>  quote
> block
"""
        self.assertEqual(block_to_block_type(block.strip()), BlockType.QUOTE)

    def test_block_type_not_quote(self):
        block = """
> This
>is
 not
> a
>  quote
> block
"""
        self.assertEqual(block_to_block_type(block.strip()), BlockType.PARAGRAPH)

    def test_block_type_unordered_list(self):
        block = """
- This
- is
- an
-  unordered
-  list
- block
"""
        self.assertEqual(block_to_block_type(block.strip()), BlockType.UNORDERED_LIST)

    def test_block_type_not_unordered_list(self):
        block = """
- This
- is
-  not
- an
-  unordered
-  list
-block
"""
        self.assertEqual(block_to_block_type(block.strip()), BlockType.PARAGRAPH)

    def test_block_type_ordered_list(self):
        block = """
1. This
2. is
3. an
4.  ordered
5.  list
6. block
"""
        self.assertEqual(block_to_block_type(block.strip()), BlockType.ORDERED_LIST)

    def test_block_type_not_unordered_list_no_period(self):
        block = """
1. This
2. is
3.  not
4. an
5.  ordered
6   list
7. block
"""
        self.assertEqual(block_to_block_type(block.strip()), BlockType.PARAGRAPH)

    def test_block_type_not_unordered_list_counter_wrong(self):
        block = """
1. This
2. is
3.  not
4. an
5.  ordered
6.   list
8. block
"""
        self.assertEqual(block_to_block_type(block.strip()), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
