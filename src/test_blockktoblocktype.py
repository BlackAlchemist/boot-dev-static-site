import unittest

from block import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_heading_level_1(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)

    def test_heading_level_6(self):
        self.assertEqual(block_to_block_type("###### Heading"), BlockType.HEADING)

    def test_heading_missing_space_not_heading(self):
        self.assertEqual(block_to_block_type("#Heading"), BlockType.PARAGRAPH)

    def test_heading_more_than_6_hashes_not_heading(self):
        self.assertEqual(block_to_block_type("####### Heading"), BlockType.PARAGRAPH)

    def test_multiline_code_block(self):
        self.assertEqual(block_to_block_type("```\nprint('hello')\n```"), BlockType.CODE)

    def test_code_block_missing_start_fence_not_code(self):
        self.assertEqual(block_to_block_type("print('hello')\n```"), BlockType.PARAGRAPH)

    def test_code_block_missing_end_fence_not_code(self):
        self.assertEqual(block_to_block_type("```\nprint('hello')"), BlockType.PARAGRAPH)

    def test_quote_block_single_line(self):
        self.assertEqual(block_to_block_type("> quote"), BlockType.QUOTE)

    def test_quote_block_multiple_lines(self):
        self.assertEqual(block_to_block_type("> line 1\n> line 2\n> line 3"), BlockType.QUOTE)

    def test_quote_block_one_bad_line_not_quote(self):
        self.assertEqual(block_to_block_type("> line 1\nline 2"), BlockType.PARAGRAPH)

    def test_unordered_list_single_line(self):
        self.assertEqual(block_to_block_type("- item 1"), BlockType.UNORDERED_LIST)

    def test_unordered_list_multiple_lines(self):
        self.assertEqual(block_to_block_type("- item 1\n- item 2\n- item 3"), BlockType.UNORDERED_LIST)

    def test_unordered_list_missing_space_not_unordered_list(self):
        self.assertEqual(block_to_block_type("-item 1"), BlockType.PARAGRAPH)

    def test_unordered_list_one_bad_line_not_unordered_list(self):
        self.assertEqual(block_to_block_type("- item 1\nitem 2"), BlockType.PARAGRAPH)

    def test_ordered_list_single_line(self):
        self.assertEqual(block_to_block_type("1. item 1"), BlockType.ORDERED_LIST)

    def test_ordered_list_multiple_lines(self):
        self.assertEqual(block_to_block_type("1. item 1\n2. item 2\n3. item 3"), BlockType.ORDERED_LIST)

    def test_ordered_list_must_start_at_1(self):
        self.assertEqual(block_to_block_type("2. item 1\n3. item 2"), BlockType.PARAGRAPH)

    def test_ordered_list_must_increment_by_1(self):
        self.assertEqual(block_to_block_type("1. item 1\n3. item 2"), BlockType.PARAGRAPH)

    def test_ordered_list_missing_space_not_ordered_list(self):
        self.assertEqual(block_to_block_type("1.item 1"), BlockType.PARAGRAPH)

    def test_plain_paragraph(self):
        self.assertEqual(block_to_block_type("This is a paragraph."), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()