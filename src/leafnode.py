from htmlnode import HTMLNode
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