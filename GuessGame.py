import random
import sys
print("                                                    Instructions.\n\n1. There are 3 Levels in this game.\n\n   (i) Easy Mode = Range from 1 to 100.\n  (ii) Medium Mode = Range from 1 to 200.\n  (iii) Hard Mode = Range from 1 to 300. ")
print("\n2. You have to choose from these levels:\n\n  (a) Enter i for Easy mode\n  (b) Enter ii for Medium mode\n  (c)Enter iii for Hard mode")
print("\n3. After choosing you have to Enter No from the range you have choosen.\n\n4. When you will choose Number the game will be end there.\n")


end = 0
while True:
    attempts = 0
    while True:
    

        choose = input("Enter for choosing the mode : ")
        if choose == 'i':
            end = 100
            print("\nYou have Choosen 'Easy Mode'.")
            break
        elif choose == 'ii':
            end = 200
            print("\nYou have choosen 'Medium Mode'.")
            break
        elif choose == 'iii':
            end = 300
            print("\nYou have choosen 'Hard Mode'.")
            break
        else:
            print("\nPlease Try again")
            continue

    Random_number = random.randint(1,end)

    while True:
        
        Player_choice = int(input("\nEnter The Number : "))
        if Player_choice>end:
            print("Please Enter Numbers from 1 to",end)
            continue
        else:
            if Player_choice == Random_number:
                print("Yes, You guessed it write.")
                attempts+=1
                break
            elif Player_choice > Random_number:
                print("You guessed large number.")
                attempts+=1
                continue
            elif Player_choice < Random_number:
                print("You have guessed small Number.")
                attempts+=1
                continue
            else:
                print("You have entered invalid Thing.\nPlease Enter Numbers only from range 1 to ",end)
            print("Current attempts : ",attempts)

    print(f"You have Taken {attempts} to guess the Number.")
    print()
    y = True
    while y == True:
        play = input("Enter (a) if you want to continue.\nEnter (b) if you want to end the game.\n") 
        if play.lower() == "a":        
            print("Okay let's Continue the game.")
            print()
            break
        elif play.lower() == "b":
            while True:
                confirmation = input("Are you sure you want to exit the game?\n1. Enter (1) to end the game. \n2. Enter (2) to continue the game\n   Enter: ")
                if confirmation == "1":
                    print("Okay, you have ended the game")
                    sys.exit()
                elif confirmation == "2":
                    print("You are continuing this game.\n")
                    y = False
                    break
                else:
                    print("Entered wrong input.\nTry again ")
                    continue
        else:
            print("Invalid input. Please enter again.")