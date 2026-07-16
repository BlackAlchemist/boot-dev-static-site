from node import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link, split_nodes_delimiter

def text_to_textnodes(text: str) -> list[TextNode]:
    new_nodes: list[TextNode]= split_nodes_image([TextNode(text, TextType.TEXT)])   #Image
    new_nodes= split_nodes_link(new_nodes)                                          #Link
    new_nodes= split_nodes_delimiter(new_nodes,"**", TextType.BOLD)                 #Bold
    new_nodes= split_nodes_delimiter(new_nodes,"_", TextType.ITALIC)                #Italic
    new_nodes= split_nodes_delimiter(new_nodes,"`",TextType.CODE)                   #Code
    return new_nodes