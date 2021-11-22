def get_formatted_name(first, last, middle = ''):
    if middle:
        full = first + ' ' + middle + " " + last
    else:
        full = first + ' ' + last
    return full.title()

def add_two(num1, num2):
    sum = num1 + num2
    return sum

#print(get_formatted_name('jodi', 'baloney','mahoganey'))

add_two(2,3)
