#3-10
#write a program that creates a list and uses all list functions in the chapter

to_do_list = ['work', 'vacation', 'startup', 'clean', 'study', 'workout', 'piano', 'invest']

to_do_list.pop()
print(to_do_list)

to_do_list.append('cityscape')
print(to_do_list)

del to_do_list[4]
print(to_do_list)

to_do_list.remove('work')

to_do_list.insert(0, 'work hard, play hard')
print(to_do_list)

# these are permanent
to_do_list.sort()
to_do_list.reverse()

# if I want to reverse sort without permanent change
print(sorted(to_do_list, reverse = True))
print(sorted(to_do_list))


