class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list[HTMLNode] = None, props: dict[str:str] = None) -> None:
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
    
