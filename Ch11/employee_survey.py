#employee survey
from survey import AnonymousSurvey

question = "Please enter employee information:"
employee_info = AnonymousSurvey(question)

employee_info.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    first = input("First name:")
    if first == 'q':
        break
    else:
        employee_info.store_response(first)
        second = input("Last name:")
        if second == 'q':
            break
        else:
            employee_info.store_response(second)
            income = input("annual salary:")
            if income == 'q':
                break
            else:
                employee_info.store_response(income)

print("Thank you for your cooperation")
employee_info.show_results()



