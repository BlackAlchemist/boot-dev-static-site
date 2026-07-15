import re
def extract_markdown_images(text: str) -> list[tuple[str,str]]:
    matches = re.findall(r"(?<=!)\[(.*?)\]\((.*?)\)",text)
    return matches

def extract_markdown_links(test: str) -> list[tuple[str,str]]:
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)",text)
    return matches