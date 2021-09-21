#5-11
#ordinal numbers

one_to_nine = [x for x in range(1,10)]
for x in one_to_nine:
    if x == 1:
        print(f"{x}st")
    elif x == 2:
        print(f"{x}nd")
    elif x == 3:
        print(f"{x}rd")
    else:
        print(f"{x}th")

