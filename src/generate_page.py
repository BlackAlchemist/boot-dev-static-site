import os
from pathlib import Path
from markdown import markdown_to_html_node, extract_title


def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str = "/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path) as from_path_file: markdown_file: str = from_path_file.read()
    with open(template_path) as template_path_file: template_file: str = template_path_file.read()
    
    markdown_html: str = markdown_to_html_node(markdown_file).to_html()

    title = extract_title(markdown_file)

    template_file= template_file.replace("{{ Title }}", title).replace("{{ Content }}", markdown_html)
    template_file= template_file.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    with open(dest_path, mode="w") as dest_file_path:
        dest_file_path.write(template_file)

def generate_page_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str = "/"):
    entries = os.listdir(dir_path_content)
    for name in entries:
        path = os.path.join(dir_path_content, name)
        if not os.path.isfile(path): generate_page_recursive(path,template_path,os.path.join(dest_dir_path,name),basepath)
        else: 
            new_dest_path = os.path.splitext(name)
            generate_page(path, template_path,os.path.join(dest_dir_path,new_dest_path[0] + ".html"),basepath)

