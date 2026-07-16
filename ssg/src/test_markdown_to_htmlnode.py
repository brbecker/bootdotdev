import unittest

from .markdown_to_htmlnode import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p>"
            "<p>This is another paragraph with <i>italic</i> text and "
            "<code>code</code> here</p></div>",
        )

    def test_headings(self):
        md = """
# This is a **bolded** H1

## This is an H2 ending with _italics_

### Boring H3

#### **Bold** H4 at beginning

##### H5

###### H6

####### H7 is just a paragraph
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a <b>bolded</b> H1</h1>"
            "<h2>This is an H2 ending with <i>italics</i></h2>"
            "<h3>Boring H3</h3>"
            "<h4><b>Bold</b> H4 at beginning</h4>"
            "<h5>H5</h5>"
            "<h6>H6</h6>"
            "<p>####### H7 is just a paragraph</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with "
            "inline stuff\n</code></pre></div>",
        )

    def test_blockquote(self):
        md = """
> This
>is
> a
>  quote
> block
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a  quote block</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- This
- is
- an
-  unordered
-  list
- block
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This</li><li>is</li><li>an</li><li> unordered</li>"
            "<li> list</li><li>block</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. This
2. is
3. an
4.  ordered
5.  list
6. block
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This</li><li>is</li><li>an</li><li> ordered</li>"
            "<li> list</li><li>block</li></ol></div>",
        )


if __name__ == "__main__":
    unittest.main()
