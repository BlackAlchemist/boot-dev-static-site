from textnode import TextNode,TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    r_list: list[TextNode]=[]
    for node in old_nodes:
        if node.text_type != TextType.TEXT: r_list.append(node)
        else:
            split_node = node.text.split(delimiter)
            if (len(split_node)%2 == 0): raise Exception("Unhandled/Invalid Markdown Syntax")
            for index, item in enumerate(split_node):
                if (index%2 == 0): r_list.append(TextNode(item,TextType.TEXT))
                else: r_list.append(TextNode(item, text_type))
    return r_list