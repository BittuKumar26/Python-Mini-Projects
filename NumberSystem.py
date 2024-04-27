choice1 = input("Your Choice increasing or decreasing : ").lower()

if "inc" in choice1:

    start = input("Starting value : ")
    end = input("Ending value : ")
    step = input("Updation value : ")
    
    choice2 = input("Row wise or column wise : ").lower()
    
    if start.isdigit() and end.isdigit() and step.isdigit():

        start = int(start)
        end = int(end)
        step = int(step)

        if step <= 0:
            print("Enter any other number greater than zero in updation.")
        elif start < end:
            for i in range(start, end + 1, step):
                if "row" in choice2:
                    print(i, end = " ")
                elif "col" in choice2:
                    print(i)  
                else:
                    print("Invalid choice. Please enter 'row' or 'column'.")  
                    break    
        elif start > end:

            temp = start
            start = end
            end = temp
            
            for i in range(end, start - 1, -step):
                if "row" in choice2:
                    print(i, end = " ")
                elif "col" in choice2:
                    print(i)  
                else:
                    print("Invalid choice. Please enter 'row' or 'column'.")  
                    break 
    else:
        print("You can only input integers.")

elif "dec" in choice1:

    start = input("Starting value : ")
    end = input("Ending value : ")
    step = input("Updation value : ")

    choice2 = input("Row wise or column wise : ").lower()
    
    if start.isdigit() and end.isdigit() and step.isdigit():

        start = int(start)
        end = int(end)
        step = int(step)

        if step <= 0:
            print("Enter any other number greater than zero in updation.")
        elif start > end:
            for i in range(start, end - 1, -step):
                if "row" in choice2:
                    print(i, end = " ")
                elif "col" in choice2:
                    print(i)  
                else:
                    print("Invalid choice. Please enter 'row' or 'column'.")  
                    break
        elif start < end:
            
            temp = start
            start = end
            end = temp
            
            for i in range(end, start + 1, step):
                if "row" in choice2:
                    print(i, end = " ")
                elif "col" in choice2:
                    print(i)  
                else:
                    print("Invalid choice. Please enter 'row' or 'column'.")  
                    break                    
    else:
        print("You can only input integers.")

else:
    print("Invalid Input. Enter a valid choice")
   