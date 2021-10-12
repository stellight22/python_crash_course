

def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        #count the number of words in alice and wonderland
        words = contents.split() #list of strings containing all words separated from white space
        num_words = len(words)
        print("The file "+ filename + " has about " + str(num_words)+ " words.")



alice = '/Users/interstellahyeon/Documents/GitHub/python_crash_course/Ch 10/Alice_in_Wonderland.txt'
moby = '/Users/interstellahyeon/Documents/GitHub/python_crash_course/Ch 10/moby_dick.txt'
sidd = '/Users/interstellahyeon/Documents/GitHub/python_crash_course/Ch 10/siddharthat.txt'
little = '/Users/interstellahyeon/Documents/GitHub/python_crash_course/Ch 10/little_women.txt'

titles = [alice, moby, sidd, little]
for title in titles:
    count_words(title)
    




