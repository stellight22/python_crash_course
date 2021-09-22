#Ch 7 while loop using a on/off flag

prompt = "\n Tell me what you want, what you really, really want."
prompt += "\n Press 'q' to quit at anytime. I will miss you."

on = True
while on:
    message = input(prompt)

    if message == 'q':
        on = False
    else:
        print(message)

        