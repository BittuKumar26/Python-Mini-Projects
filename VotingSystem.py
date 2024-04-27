print("============================= Welcome to the Voting Machine ===================================")

vote_1 = 0
vote_2 = 0
vote_3 = 0
vote_4 = 0

while True:
    n = int(input("Enter your age : "))
    
    if n < 18:
        a = 18-n
        print("You are not eligible to vote. \nTry after",a,"Years")
        
    else:
        print("You are eligible to vote")
    
        print("There are 4 options to which you can vote.You have to enter Number of party you want to vote. \n1. Bhartiye Janta Party.\n2. Aam Aadmi party. \n3. Congress \n4. No One I want to vote myself ")
        
        vote = int(input("Enter the party Number : "))
        
        if vote == 1:
            print("Are you sure you want to vote Bhartiye Janta Party?")
            confirm_1 = input("Enter Y or N : ")

            if confirm_1.capitalize() == "Y":
                print("You have given your vote to Bhartiye janta party.")
                vote_1 += 1
                
            elif confirm_1.capitalize() == "N":
                print("Okay choose again")
                continue
        elif vote == 2:
            print("Are you sure you want to vote Aam Aadmi Party?")
            confirm_1 = input("Enter Y or N : ")
            if confirm_1.capitalize() == "Y":
                print("You have given your vote to Aam aadmi party.")
                vote_2 += 1
            
            elif confirm_1.capitalize() == "N":
                print("Okay choose again")
                continue
        elif vote == 3:
            print("Are you sure you want to vote Congress?")
            confirm_1 = input("Enter Y or N : ")
            if confirm_1.capitalize() == "Y":
                print("You have given your vote Congress.")
                vote_3 += 1
                
            elif confirm_1.capitalize() == "N":
                print("Okay choose again")
                continue
        elif vote == 4:
            
            print("Are you sure you want to give your vote to Yourself")
            confirm_1 = input("Enter Y or N : ")
            
            if confirm_1.capitalize() == "Y":
                print("You have given your vote to Yourself.")
                vote_4 += 1
                
            elif confirm_1.capitalize() == "N":
                print("Okay choose again")
                continue
        else:
            print("Invalid please Try again")
            continue
        
        print("------------Break Point------------")

    Loop  = int(input("Enter 1 if you want to continue. \nEnter 2 if you want to End it \n : "))
    
    if Loop == 1:
        continue
    elif Loop == 2:
        break
    else:
        print("Inavlid please enter again")
        break


print("Vote of Bhartiye janta Party are =",vote_1)
print("Vote of Aam Aadmi party are =",vote_2)
print("Vote of the Congress are =",vote_3)
print("vote of yourself are =",vote_4)