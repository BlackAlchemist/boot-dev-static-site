import re
def extract_markdown_images(text: str) -> list[tuple[str,str]]:
    matches = re.findall(r"(?<=!)\[(.*?)\]\((.*?)\)",text)
    return matches

def extract_markdown_links(text: str) -> list[tuple[str,str]]:
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)",text)
    return matches

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks