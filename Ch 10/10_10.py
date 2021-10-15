filename = "/Users/interstellahyeon/Documents/GitHub/python_crash_course/Ch 10/the.txt"

def extra_work():
    try:
        with open(filename) as f_o:
            words = f_o.read()
            print(words)
            print(words.count('bap'))
    except FileNotFoundError:
        print("The file the.txt does not exist")
 

extra_work()
    
