#fillinf a dictionary with user input part 2

dictionary_name = {}
switch_on = True

while switch_on:
    name = input("Name:\n")
    ans = input("Response: \n")

    dictionary_name[name] = ans

    ask_again = input("Do you want to enter another round?")
    if ask_again == 'N':
        switch_on = False
#print out results

print("--Results--")
for name, ans in dictionary_name:
    print(name + " responded "+ ans)

    