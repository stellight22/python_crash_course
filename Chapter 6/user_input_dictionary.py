#Filling a dictionary with user input

responses = {}

polling_active = True

while polling_active:
    name = input("What is your name?\n")
    response = input("What is your favorite comfort food?\n")
    #setting up key and value
    responses[name] = response

    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':   # turn off loop
        polling_active = False

#show results at end
#print out contents of dictionary
print("\n --Polling Results--")
for name, response in responses.items():
    print(name + "would like to eat "+ response + " for Sunday brunch.")