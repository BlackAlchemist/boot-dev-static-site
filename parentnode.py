from htmlnode import HTMLNode

class ParentNode():
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


