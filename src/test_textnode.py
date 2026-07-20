import unittest
from node import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "HTTPS://URL_TESTING")
        self.assertEqual(str(node),"TextNode(This is a text node, bold, HTTPS://URL_TESTING)")
    
    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)
    
    def test_text_type(self):
        node = TextNode("This is a text node", "bold")
        self.assertNotEqual(node.text_type, TextType.BOLD)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()