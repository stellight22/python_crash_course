#3-7
guest_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("The reservation did not go through and only two people can join for dinner.")

guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()

print(guest_list)
for guest in guest_list:
    print(f"Dear {guest}, your table is ready.")

del guest_list[0]
print(guest_list)
del guest_list[0]
print(guest_list)