import os, shutil, sys

from copystatic import copy_files_recursive
from generate_page import generate_page_recursive

dir_path_static = "./static"
dir_path_docs = "./docs"
if len(sys.argv) >= 2:
    basepath = sys.argv[1]
else:
    basepath ="/"


def main() -> None:
    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    generate_page_recursive("./content","./template.html",dir_path_docs,basepath)


main()
