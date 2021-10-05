#3-5
#continuing from 3-4
#one of the guests can't make it
#replace the guest with newbie
#reprint invitations

guest_list = ['Rihanna', 'Drake', 'JLo']
for guest in guest_list:
    print(f"Dear {guest.title()}, you have been invited.")

print(f"The original guest {guest_list[0]} cannot make it, so")
guest_list.remove('Rihanna')
guest_list.insert(0,'Marilyn monroe')

print(f"Instead, {guest_list[0].title()} will be joining us!")

for guest in guest_list:
    print(f"Here enters {guest.title()}. A round of applause!")

    