#7-10

poll_results = []
question = "Where is your dream vacation? "
question += "Enter 'q' to quit. "
answer = ""
while answer != 'q':
    answer = input(question)
    if answer != 'q':
        poll_results.append(answer)

print("Display results:")
print(poll_results)
