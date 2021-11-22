cats = "/Users/interstellahyeon/Documents/GitHub/python_crash_course/Ch 10/cats.txt"
dogs = "/Users/interstellahyeon/Documents/GitHub/python_crash_course/Ch 10/dogs.txt"


def animal_names(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
        print(contents)
    except FileNotFoundError:
        pass


animal_names(cats)
animal_names(dogs)
