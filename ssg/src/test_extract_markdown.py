import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)."
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "This is text with ![image](https://i.imgur.com/zjjcJKZ.png) and "
            "![image2](https://www.boot.dev/img/bootdev-logo-full-150.png)."
        )
        self.assertListEqual([
            ("image", "https://i.imgur.com/zjjcJKZ.png"),
            ("image2", "https://www.boot.dev/img/bootdev-logo-full-150.png"),
        ], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [boot.dev](https://www.boot.dev)."
        )
        self.assertListEqual([("boot.dev", "https://www.boot.dev")], matches)

    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "This is text with links [boot.dev](https://www.boot.dev) and "
            "[google](https://www.google.com)."
        )
        self.assertListEqual([
            ("boot.dev", "https://www.boot.dev"),
            ("google", "https://www.google.com"),
        ], matches)

    def test_extract_markdown_images_both(self):
        matches = extract_markdown_images(
            "This is text with image ![image](https://i.imgur.com/zjjcJKZ.png) and "
            "link [google](https://www.google.com)."
        )
        self.assertListEqual([
            ("image", "https://i.imgur.com/zjjcJKZ.png"),
        ], matches)

    def test_extract_markdown_links_both(self):
        matches = extract_markdown_links(
            "This is text with image ![image](https://i.imgur.com/zjjcJKZ.png) and "
            "link [google](https://www.google.com)."
        )
        self.assertListEqual([
            ("google", "https://www.google.com"),
        ], matches)


if __name__ == "__main__":
    unittest.main()
