#7-4 while loops
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#letting user choose when to quit

question = "\n Tell me what you want, what you really, really want."
question += "\n Enter 'q' to quit at any time."

#this is to store user's response
answer = ""

#outer loop dependent on user response, negative
while answer != 'q':
    answer = input(question)
    print(answer)

#before fixing:
prompt = "\nTell me something, and I will repeat."
prompt += "\nEnter 'q' to quit."

response = ""
while response != 'q':
    response = input(prompt)
    print(response)

#after fixing so the program doesn't repeat out 'q'

prompt = "\nTell me something, and I will repeat."
prompt += "\nEnter 'q' to quit."

response = ""
while response != 'q':
    response = input(prompt)

    if response != 'q':
        print(prompt)

    