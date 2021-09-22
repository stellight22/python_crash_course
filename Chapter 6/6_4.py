#6-4 Glossary 2

from os import path


py_glossary = {
    'Chapter 3': 'lists', 
    'Ch 4': 'List functions',
    
}
for k, v in py_glossary.items():
    print(f"The order of textbook is {k} : {v}")

py_glossary['ch5'] = 'if statements'
py_glossary['ch6'] = 'dictionaries'
py_glossary['ch7'] = 'while loops'
py_glossary['ch 8'] = 'functions'
py_glossary['ch9'] = 'classes'
py_glossary['ch10'] = 'files and exceptions'    

print(py_glossary.items())

for k, v in py_glossary.items():
    print(f"The order of textbook is {k} : {v}")