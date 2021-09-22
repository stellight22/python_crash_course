#Ch 7 using break to exit a loop

prompt = "\n Tell me what you want, what you really, really want."
prompt += "\n Press 'q' to quit at anytime. I will miss you."

while True:
    city = input(prompt)

    if city == 'q':
        break
    else:
        print("I will go to "+ city.title()+ " today!")
        