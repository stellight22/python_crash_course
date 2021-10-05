#6-3 glossary
py3_dict = {
    'list': '[ordered collection of objects]', 
    'tuple': '(fixed list)', 
    'set': '{unique items}',
    'PEP8': 'syntax guideline', 
    'indentation': 'control flow',
}
"""
Print each word and its meaning as neatly formatted output . 
You might print the word followed by a colon and then its meaning, 
or print the word on one line and then print its meaning indented on a 
second line . Use the newline character (\n) 
to insert a blank line between each word-meaning pair in your output .
"""

for term, significance in py3_dict.items():
    print(f"\nThe word {term} is important in python as it's used for {significance}.")
