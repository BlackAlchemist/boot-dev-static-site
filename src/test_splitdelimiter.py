import unittest
from split_nodes import split_nodes_delimiter
from node import TextNode,TextType

class TestSplitDelimiter(unittest.TestCase):
    def test_normal_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),TextNode("code block", TextType.CODE),TextNode(" word", TextType.TEXT),])
    # def test_multiple_split(self):
    #     pass
    # def test_no_delimiter(self):
    #     pass
    # def test_non_text_node(self):
    #     pass
    # def test_mismatch(self):
    #     pass
    # def test_delimiter_start(self):
    #     pass
