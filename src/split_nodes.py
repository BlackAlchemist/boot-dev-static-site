from node import TextNode, TextType
from extract_markdown import extract_markdown_images,extract_markdown_links

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    r_list: list[TextNode]=[]
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT: r_list.append(old_node)
        else:
            original_text = old_node.text
            found_links = extract_markdown_images(old_node.text)
            for link in found_links:
                sections = original_text.split(f"![{link[0]}]({link[1]})", 1)
                if len(sections) != 2: raise ValueError("invalid markdown, link section not closed")
                if sections[0] != "": r_list.append(TextNode(sections[0], TextType.TEXT))
                r_list.append(TextNode(link[0], TextType.IMAGE, link[1]))
                original_text = sections[1]
            if original_text != "": r_list.append(TextNode(original_text,TextType.TEXT))
    return r_list   

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    r_list: list[TextNode]=[]
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT: r_list.append(old_node)
        else:
            original_text = old_node.text
            found_links = extract_markdown_links(old_node.text)
            for link in found_links:
                sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
                if len(sections) != 2: raise ValueError("invalid markdown, link section not closed")
                if sections[0] != "": r_list.append(TextNode(sections[0], TextType.TEXT))
                r_list.append(TextNode(link[0], TextType.LINK, link[1]))
                original_text = sections[1]
            if original_text != "": r_list.append(TextNode(original_text,TextType.TEXT))
    return r_list
            
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