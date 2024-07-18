import os

from docx import Document
from typing import List


keyWords = {"错", "难"}
directory = r"D:\files\数学"


def read_docx(file_path) -> List:
    doc = Document(file_path)
    docxContent = []
    for para in doc.paragraphs:
        docxContent.append(para.text)
    return docxContent


def isKeyWordInDocx(docxContent: List) -> bool:
    for line in docxContent:
        for keyWord in keyWords:
            if keyWord in line:
                return True


def find_docx_files(directory):
    docx_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.docx'):
                docx_paths.append(os.path.join(root, file))
    return docx_paths


def main():
    docx_paths = find_docx_files(directory)
    # allDocxsPathAndContent = dict()
    for docxPath in docx_paths:
        if isKeyWordInDocx(read_docx(docxPath)):
            print(docxPath)



if __name__ == "__main__":
    # file_path = r"D:\files\数学\代数\不等式.docx"
    # content = read_docx(file_path)
    # print(isKeyWordInDocx(content))
    # print(content)

    main()
