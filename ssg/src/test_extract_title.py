import unittest

from textwrap import dedent

from .extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title_simple(self):
        result = extract_title(
            "# Title"
        )
        self.assertEqual(result, "Title")

    def test_extract_title_mixed(self):
        result = extract_title(dedent("""\
                ## H2
                ### H3
                # Title
            """))
        self.assertEqual(result, "Title")

    def test_extract_title_extra_spaces(self):
        result = extract_title(
            "#    Title    "
        )
        self.assertEqual(result, "Title")

    def test_extract_title_missing(self):
        self.assertRaises(
            ValueError,
            extract_title,
            dedent("""\
                ## H2
                ### H3
                #### H4
            """)
            )
