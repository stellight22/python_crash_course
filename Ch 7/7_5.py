#7-5 movie tickets
"""
A movie theater charges differentg ticket prices 
depending on a person's age
write a loop in which you ask users their age, and then 
tell them the cost of their movie ticket.
"""

prompt = "enter the person's age:"
prompt += "Enter 'q' to quit."

total = 0


on = True
while on:
    answer = input(prompt)
    if answer != 'q':
        if int(answer) <3:
            total += 0
        elif int(answer) >= 3 and int(answer) <= 12:
            total += 10
        elif int(answer) >12:
            total+= 15
        else:
            print("error")
    else:
        on = False
    print("The total is:")
    print(total)


