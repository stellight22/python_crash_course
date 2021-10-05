#name formatting functions

#all three names required:
def get_formatted_name(f_name, m_name, l_name):
    full_name = f_name + " " + m_name + " " + l_name
    return full_name.title()

person = get_formatted_name('queen','bohemian', 'rhapsody')
print(person)

def incomplete_name_input(f_name, l_name, m_name = ''):
    #if middle name is inputted
    if m_name:
        full_name = f_name + ' '+ m_name + ' ' + l_name
    else:
        full_name = f_name + ' '+ l_name
    return full_name.title()

m_person = incomplete_name_input('adam', 'levine','austin')
person_no_middle = incomplete_name_input('justin', 'timberlake')

print(m_person)
print(person_no_middle)
