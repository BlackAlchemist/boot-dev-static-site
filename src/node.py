from enum import Enum
class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

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

class HTMLNode:
    def __init__(self, tag: str | None = None, value: str | None = None, children: list[HTMLNode] | None = None, props: dict[str:str] | None = None) -> None:
        self.tag: str | None = tag
        self.value: str | None = value
        self.children: list[HTMLNode] | None = children
        self.props: dict[str:str] | None = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        return_string: str = ""
        if self.props == None: return return_string
        for key, value in self.props.items():
            return_string+= f" {key}={value}"
        return return_string
    
    def __repr__(self) -> str:
        return f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict[str:str] = None) -> None:
        super().__init__(tag,value,None,props)
    
    def to_html(self):
        if self.value == None: raise ValueError("Leaf: Value is None")
        if self.tag == None: return self.value

        start = f"<{self.tag}>"
        end = f"</{self.tag}>"

        if self.tag == "a":
            temp: str =""
            for key, value in self.props.items():
                temp+=f"<a {key}=\"{value}\">{self.value}{end}"
            return temp
        
        return f"{start}{self.value}{end}"
    
    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nProps: {self.props}"
    
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str:str] = None) -> None:
        super().__init__(tag= tag,value= None,children= children,props= props)
    
    def to_html(self) -> str:
        if self.tag == None: raise ValueError("Parrent Node is missing Tag")
        if self.children == None: raise ValueError("Parent Node is missing children")
        start = f"<{self.tag}>"
        end = f"</{self.tag}>"

        temp= start
        for child in self.children:
            temp+=child.to_html()
        temp+= end
        return temp
    
