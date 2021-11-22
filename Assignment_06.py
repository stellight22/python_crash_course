"""
Assignment Six: Recursion Using Bubble Sort
Submitted by Ahyeon Cho
Submitted: October 31st 2021

Sort sensor list by room number and by name using bubble sort
"""

def recursive_sort(list_to_sort, key = 0):
    
    my_listt = list_to_sort[:]
    length = len(my_listt)
    #base case
    
    if length == 1:
        return my_listt
    else:
        if key == 0:
            for x in range(0, len(my_listt)-1): 
                if my_listt[x] < my_listt[x+1]:
                    my_listt[x], my_listt[x+1] = my_listt[x+1], my_listt[x]
            q = my_listt.pop()
            my_listt = recursive_sort(my_listt) #key default is 0
            my_listt.insert(0,q)
            return my_listt

        if key == 1:
            for x in range(0, len(my_listt)-1): 
                if my_listt[x][1][0] < my_listt[x+1][1][0]: #the first letter in name
                    my_listt[x], my_listt[x+1] = my_listt[x+1], my_listt[x]
            q = my_listt.pop()
            my_listt = recursive_sort(my_listt,1) 
            my_listt.insert(0,q)
            return my_listt


def convert_units(celsius_value, units):
    if units == 0:
        return float(celsius_value)
    elif units == 1:
        fahrenheit = (float(celsius_value) * (9 / 5)) + 32
        return fahrenheit
    elif units == 2:
        kelvin = float(celsius_value) + 273.15
        return kelvin


def print_menu():
    print("Main Menu")
    print("---------")
    print("1 - Process a new data file")
    print("2 - Choose units")
    print("3 - Edit room filter")
    print("4 - Show summary statistics")
    print("5 - Show temperature by date and time")
    print("6 - Show histogram of temperatures")
    print("7 - Quit")


def new_file(dataset):
    """ Open a new file"""
    print("New file Function Called")


def choose_units():
    """Allows user to choose units"""
    print("Choose Units Function Called")


def change_filter(sensor_list, active_sensors):
    """ Allows user to change filters"""
    print("Change Filter Function Called")


def print_summary_statistics(dataset, active_sensors):
    """ Prints summary of statistics"""
    print("Summary Statistics Function Called")


def print_temp_by_day_time(dataset, active_sensors):
    """ Print temperature by daytime"""
    print("Print Temp by Day/Time Function Called")


def print_histogram(dataset, active_sensors):
    """ Print histogram"""
    print("Print Histogram Function Called")


def main():
    #dictionary creation from sensors
    sensors = {
        '4213': ("STEM Center", 0),
        '4201': ("Foundations Lab", 1),
        '4204': ("CS Lab", 2),
        '4218': ("Workshop Room", 3),
        '4205': ("Tiled Room", 4),
        'Out': ("Outside", 10)

    }

    #list of tuples comprehension
    sensor_list = [(room_num, sensor_list[0], sensor_list[1]) for room_num, sensor_list in sensors.items()]


    #Test Case
    print("\nOriginal unsorted list\n", sensor_list)
    print("\nList sorted by room number\n",recursive_sort(sensor_list, 0))
    print("\nList sorted by room name\n", recursive_sort(sensor_list, 1))
    print("\nOriginal unsorted list\n", sensor_list)
       

    print("STEM Center Temperature Project")
    print("Ahyeon Stella Cho")
    while True:
        print_menu()
        try:
            prompt_key = int(input("What is your choice? "))
        except ValueError:
            print("*** Please enter a number only ***")
        else:
            if int(prompt_key) < 1 or int(prompt_key) > 7:
                print("Invalid Choice")
            if prompt_key == 1:
                new_file(None)
            if prompt_key == 2:
                choose_units()
            if prompt_key == 3:
                change_filter(None, None)
            if prompt_key == 4:
                print_summary_statistics(None, None)
            if prompt_key == 5:
                print_temp_by_day_time(None, None)
            if prompt_key == 6:
                print_histogram(None, None)
            if prompt_key == 7:
                print("Thank you for using the STEM Center Temperature Project")
                break


if __name__ == "__main__":
    main()


"""
(base) Stellas-MBP:Course_CS_3A interstellahyeon$  cd /Users/interstellahyeon/Documents/GitHub/Course_CS_3A ; /usr/bin/env /usr/local/bin/python3 /Users/interstellahyeon/.vscode/extensions/ms-python.python-2021.10.1365161279/pythonFiles/lib/python/debugpy/launcher 50661 -- /Users/interstellahyeon/Documents/GitHub/Course_CS_3A/Assignments/6.py 

Original unsorted list
 [('4213', 'STEM Center', 0), ('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4218', 'Workshop Room', 3), ('4205', 'Tiled Room', 4), ('Out', 'Outside', 10)]

List sorted by room number
 [('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4205', 'Tiled Room', 4), ('4213', 'STEM Center', 0), ('4218', 'Workshop Room', 3), ('Out', 'Outside', 10)]

List sorted by room name
 [('4204', 'CS Lab', 2), ('4201', 'Foundations Lab', 1), ('Out', 'Outside', 10), ('4213', 'STEM Center', 0), ('4205', 'Tiled Room', 4), ('4218', 'Workshop Room', 3)]

Original unsorted list
 [('4213', 'STEM Center', 0), ('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4218', 'Workshop Room', 3), ('4205', 'Tiled Room', 4), ('Out', 'Outside', 10)]
STEM Center Temperature Project
Ahyeon Stella Cho
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice? 7
Thank you for using the STEM Center Temperature Project
(base) Stellas-MBP:Course_CS_3A interstellahyeon$ 
"""




