#3-6
#add three more guests to the dinner table

guest_list = ['marilyn monroe', 'Drake', 'JLo']
print("Dear guests, we have a bigger table ready for us!")

#use insert() to add one new guest to beginning of the list
guest_list.insert(0, 'Jeyeon')
#use insert() to add one new guest in middle
guest_list.insert(3, 'Captain jack')
#use append() to add one new guest in end
guest_list.append('Babe the Pig')

for guest in guest_list:
    print(f"Good evening, {guest.title()}. Welcome to the table.")
