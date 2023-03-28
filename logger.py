import PyPDF2
import re
import io
import os

def parsePage(page_obj):
    page_text = page_obj.extract_text()
    matches = ["diamond", "libsysdev", "libtest", "libutil", "request"]
    for line in io.StringIO(page_text):
        if any([x in line for x in matches]):
            print(line)
            
file_names = os.listdir('./docs')
for file_name in file_names:
    print(file_name + ": \n")
    file_obj = open("./docs/" + file_name, 'rb')
    pages_obj = PyPDF2.PdfReader(file_obj).pages   
    for page_obj in pages_obj:
        parsePage(page_obj)
    print("---------------------------------------")
    