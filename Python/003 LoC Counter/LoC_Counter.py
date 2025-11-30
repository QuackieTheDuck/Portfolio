# count LoC, exclude comments, save progress to file(CSV/JSON)
# need to check what additions are in post course exercieses
# concern displaying stats in HTML website

import os
import time

# create a library of languages(concern only known)
# get Patah
# get time
# walk thorugh folders and files
# save stats to a dir

lang={
    "c":"C/C++",
    "cpp":"C/C++",
    "h":"C/C++",
    "hpp":"C/C++",
    "hxx":"C/C++",
    "cc":"C/C++",
    "cxx":"C/C++",
    "py":"Python",
    "pyz":"Python",
    "pyc":"Python",
    "pyo":"Python",
    "rs":"Rust",
    "js":"JavaScript",
    "JS":"JavaScript",
    "md":"Markdown",
    "bat":"Batch",
    "ino":"Arduino",
    "pyw":"Python",
    "pl":"Perl",
    "php":"PHP",
    "php3":"PHP",
    "php4":"PHP",
    "php5":"PHP",
    "mk":"Makefile",
    "s":"Assembly",
    "as":"Assembly",
    "asm":"Assembly",
    "ps1":"PowerShell",
    "rd":"Ruby",
    "kt":"Kotlin",
    "java":"Java",
    "sh":"Shell/Bash",
    "cs":"C#",
    "html":"HTML",
    "htm":"HTML",
    "ts":"TypeScript",
    "cmd":"PowerShell",
}

loc={}
def get_date():
    print(time.strftime("%H:%M, %d.%m.%Y"))
#get_date()


def list_files():
    path=os.getcwd()
    for root, dirs, files in os.walk(path):
        for i in range (0, len(files)):
            if (a:=str(files[i].split('.')[-1])) in lang:
                print(files[i], "<--", lang.get(a))

list_files()