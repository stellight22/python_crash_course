#8-11
magician_names = ['drew', 'stone sparkles', 'river ka']


def show_magicians(magician_names):
    for magician in magician_names:
        print(magician.title())

def make_great(magician_names):
    for magic in magician_names:
        magic = "The Great " + magic.title()
        print(magic)
        
show_magicians(magician_names)
make_great(magician_names[:])

print(magician_names)

