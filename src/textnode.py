from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "**bold**"
    ITALIC = "_italic_"
    CODE = "`code`"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text: str = text
        self.text_type: TextType = text_type
        self.url: str | None = url
        
    def __eq__(self, other: TextNode):
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def text_node_to_html_node(text_node: TextNode) -> LeafNode:
        match text_node.text_type:
            case TextType.TEXT:
                return LeafNode(tag= None, value=text_node.text)
            case TextType.BOLD:
                return LeafNode(tag="b",value=text_node.text)
            case TextType.ITALIC:
                return LeafNode(tag="i",value=text_node.text)
            case TextType.CODE:
                return LeafNode(tag="code",value=text_node.text)
            case TextType.LINK:
                return LeafNode(tag="a",value=text_node.text,props={"href": "https://google.com"})
            case TextType.IMAGE:
                return LeafNode(tag="img",value="",props={"src": "image url", "alt": "alt text"})
            case _:
                raise Exception("Invalid Text Type")