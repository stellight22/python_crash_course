#using a continue

current = 0
while current <10:
    current += 1
    if current % 2 == 0:
        continue #means skip
    print(current)

#1,3,5,7,9

current2 = 1
while current2 < 11:
    current2 += 1
    if current2 %2 == 1:
        continue #means skip odd nums
    print(current2)
#output: 2,4,6,8,10

current3 = 0
while current3 <30:
    current3 += 3
    if current3 %2 == 0:
        continue
    print(current3)
#output: 3,9,15,21,27
#doesn't have 6,12,24

while current3 < 60:
    current3 +=3
    if current3 %2 ==1:
        continue
    print(current3)
#36, 42, 48, 54, 60
