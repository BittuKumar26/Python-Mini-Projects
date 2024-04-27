def calculaor(data):
    try:
        result = eval(data)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

while True:
    user = input("Enter what to calculate (or 'exit' to discontinue): ")

    if user.lower() == 'exit':
        print("You are Welcome Again!")
        break

    result = calculaor(user)
    print("Result:", result)



