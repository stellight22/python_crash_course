#3-3

weekend_activities =['brunch', 'shopping', 'gym', 'write', 'read', 'cafe']
counter = 0
for activity in weekend_activities:
    if counter == 0:
        print("On a lazy Sunday, I start late with "+ weekend_activities[counter])
        counter += 1
    elif counter == 1:
        print(" and then I do some" + weekend_activities[counter])
        counter +=1
    elif counter ==2:
        print("Then I go change at home and go to the "+ weekend_activities[counter])
        counter +=1
    elif counter == 3:
        print("After the gym, I shower and "+ weekend_activities[counter]+ " in order to reflect the past week and plan the next.")
        counter +=1
    elif counter ==4:
        print("I might also go "+ weekend_activities[counter])
        counter +=1
    elif counter == 5:
        print(" at the local "+ weekend_activities[counter]+ " located near Stanford.")

#easier way

print(f"statement1 {weekend_activities[0]}, statement2 {weekend_activities[1]}")

# or
statement1 = f"something {weekend_activities[0]}"
statement2 = f"something {weekend_activities[1]}"

print(statement1+" "+ statement2)
#or
print(f"Short Story \n{statement1} {statement2}")