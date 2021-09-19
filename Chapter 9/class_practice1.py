class Student:
    def __init__(self, ID, major):
        self.ID = ID
        self.major = major

    def login(self):
        print("Welcome to class portal")
        print("Hello, student "+ self.ID + "!. Welcome back.")

    def homepage(self):
        print("This is the college of" + self.major+ " class page.")

student_j = Student(7743, 'computer science')
