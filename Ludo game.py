from random import randint

com_sum = 0
user_sum = 0

while True:
    
    user = int(input('Your dice no. :'))
    if 1 <= user <= 6:
        com = randint(1, 7)
    
        print('Computer generated:',com)
    
        com_sum += com
        user_sum += user
    
        choice = input('Want to continue? (y/n):').lower()
    
        if choice == "y":
            continue
        else:
            break
    else:
        while True:
            print(f'{user} is Invalid dice no. Please Input again')
            user = int(input('Your dice no. :'))
            if 1 <= user <= 6:
                com = randint(1, 7)
                print('Computer generated:',com)
                break
    
        com_sum += com
        user_sum += user
    
        choice = input('Want to continue? (y/n):').lower()
    
        if choice == "y":
            continue
        else:
            break
            
                 

if user_sum > com_sum:
    print("User won")
elif user_sum < com_sum:
    print('Computer won')   
else:
    print('Match draw')
    



    