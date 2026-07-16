import unittest
from node import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode()

        dict_test = {"href": "https://www.google.com","target": "_blank",}
        list_test = list[node]

        node2 = HTMLNode("Tag Test", "Value Test", list_test, dict_test)

        self.assertEqual(node.tag, None)
        self.assertEqual(node2.props, dict_test)

    def test_to_html(self):
        pass

    def test_props_to_html(self):
        props_test = {"href": "https://www.google.com","target": "_blank",}
        node = HTMLNode(props=props_test)

        self.assertNotEqual(node.props_to_html(),"")

        
    def test_repr(self):
        dict_test = {"href": "https://www.google.com","target": "_blank",}

        node = HTMLNode()
        self.assertEqual(str(node), f"Tag: {node.tag}\nValue: {node.value}\nChildren: {node.children}\nProps: {node.props}")