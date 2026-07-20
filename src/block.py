from enum import Enum
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown: str) -> BlockType:
    match (markdown[0]):
        case "#": #Heading Check
            num = 0
            for character in markdown:
                if character == "#": 
                    num+=1
                    continue
                if character == " " and 1<=num<=6: return BlockType.HEADING
                else: break
        case "`": #Code Check
            if markdown.startswith("```\n") and markdown.endswith("```"): return BlockType.CODE
        case ">": #Quote Check
            quote_check = markdown.split("\n")
            for sub_string in quote_check:
                if sub_string.startswith(">"): continue
                else: return BlockType.PARAGRAPH
            return BlockType.QUOTE
        case "-": #Unordered Check
            unordered_check = markdown.split("\n")
            for sub_string in unordered_check:
                if sub_string.startswith("- "): continue
                else: return BlockType.PARAGRAPH
            return BlockType.UNORDERED_LIST
        case "1":
            ordered_check = markdown.split("\n")
            prev_num = 1
            for sub_string in ordered_check:
                if sub_string.startswith(f"{prev_num}. "):
                    prev_num += 1
                    continue
                else: return BlockType.PARAGRAPH
            return BlockType.ORDERED_LIST
        case _:
            pass
    return BlockType.PARAGRAPH
