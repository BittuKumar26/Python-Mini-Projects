def readMode():
    myFile = open("system.txt", "r")
    dict = eval(myFile.read())
    myFile.close()
    return dict

def writeMode(data):
    myFile = open("system.txt", "w")

    myFile.write(str(data))

    myFile.close()

def displayStudent():
    print('Ids of Students available:')
    for index, ids in enumerate(data):
        print(f'{index+1}: {ids}')

    id = int(input("\nWhich id's details you would like to see: "))

    if id not in data:
        print('This Student ID does not Exist!!')
    else:     
        student = data.get(id)
        print(f'\n{'-' * 30}')
        print(f'Name: {student[0]}')
        print(f'Section: {student[1]}')
        print(f'Roll Number: {id}')
        print(f'CPI: {student[2]}')
        print(f'{'-' * 30}')

def addStudent():
    id = int(input('\nEnter Student Id(Roll no.): '))
    if id in data:
        print('This ID already exists!! Cannot add new Student with same ID.')
    else:    
        detail = input('Enter your details(Ex.Name, Section, CPI): ').split(',')
        data[id] = detail
        print('New Student is Added Successfully!!')

def updateStudent():
    id = int(input('\nEnter your Student Id you want to update: '))
    if id not in data:
        print('This Student ID does not Exist!!')
    else:     
        detail = input('Enter your details(Ex.Name, Section, CPI): ').split(',')
        data[id] = detail
        print('Existing Student is Updated Successfully!!')

def deleteStudent():
    id = int(input('\nEnter which Student Id you want to delete: '))
    if id not in data:
        print('This Student ID does not exist!!')
    else:
        del data[id]
        print('Student is Deleted Successfully!!')

data = readMode()

while True:
    print(f'\n{'='*40}\n')   

    print(
      '1. Display Student Details',
      '2. Add a new Student',
      '3. Update a Student Detail',
      '4. Delete an existing Student',
      '5. Exit', sep='\n'
      )
    
    user_choice = int(input('\nEnter Your Choice: '))
    
    if user_choice == 1:
        displayStudent()
    elif user_choice == 2:
        addStudent()
    elif user_choice == 3:
        updateStudent()
    elif user_choice == 4:
        deleteStudent()
    elif user_choice == 5:
        print(f'{'-' * 30}')
        print('Thanks for using this software!!')
        print(f'{'-' * 30}')
        break
    else:
        print('Invalid Choice!!')    
        
writeMode(data)


