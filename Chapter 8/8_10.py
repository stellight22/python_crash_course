#8-10 great magicians

magician_names = ['drew', 'stone sparkles', 'river ka']

def show_magicians():
    for magician in magician_names:
        print(magician.title())

def make_great():
    for magician in magician_names:
        print("The Great " + magician.title())
        
show_magicians()
make_great()

