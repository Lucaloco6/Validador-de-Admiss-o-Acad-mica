#em inglês!!
import os

candidates = []

def validate_and_add_candidate(name, age, courses):
    if int(age) >= 18 and int(courses) >= 5:
        print(f'{name} was Elected!!')
        candidates.append({
            'name':name,
            'age':age,
            'number_of_courses':courses
        })
    else:
        print(f'{name} was not elected because they' \
        ' does not meet the requirements. sorry.')

def list_candidates():
    for i in candidates:
        print(f"Name: {i['name' \
        '']}, Age:{i['age' \
        '']}, Courses:{i['number_of_courses']}")
    
while True:

    print("do you want to exit? (yes) ou (no) ")
    sair = input()
    if sair.lower() == 'yes' or sair.lower() == 'sim':
        break

    student_name = (input('enter the student name, here: '))
    student_age = (input('enter the student age, here: '))
    number_of_courses = (input('enter the number of courses, here: '))
    
    try:
        student_age.isdigit() == True
        number_of_courses.isdigit() == True
    except ValueError as e:
        print(f'ONLY NUMBERS PLEASE: {e}')

    if student_name.isdigit() == True:
        print(f'IN THE NAME INPUT YOU DID NOT TYPE A WORD  ')
    else:
        os.system('cls')
        validate_and_add_candidate(
        student_name, student_age, number_of_courses
        ) 
        print('elected candidates:')   
        list_candidates()
        print('\n')
