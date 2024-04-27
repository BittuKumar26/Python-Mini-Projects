
all_products = {
    "Chips":10, 
    "Soft drink":100,
    "Popcorn":45,  
    "Pretzel":120, 
    "Candy bar":10, 
    "Nut":20,
    "Water":20, 
    "Coffee":50, 
    "Tea":20, 
    "Energy drink":120,
    "Burger":50, 
    "Pizza":150, 
    "Hot dog":60, 
    "Sandwiches":45, 
    "French fries":30,
    "Ice cream":35, 
    "Cookie":70, 
    "Cake":250, 
    "Pastrie":40, 
    "Donut":60,
    "Sushi":300, 
    "Taco":350, 
    "Curry":150, 
    "Spring roll":30,
    "Salad":200, 
    "Smoothie":150, 
    "Yogurt parfait":135, 
    "Chocolate":80,
    }

balance = int(input("What's your card balance:"))

for product, price in all_products.items():
    print(f"{product}:{price}₹")

n = int(input('How many products you want to buy? :'))

buying = {}

print('Name the items you want to buy:')
for product in range(1, n+1):
    item = input(f'Item {product}:').capitalize()
    quantity = int(input('Quantity:'))
    if item not in all_products:
        while True:
            print(f'{item} is not available. Please enter a valid product.')
            item = input(f'Item {product}:').capitalize()
            quantity = int(input('Quantity:'))
            if item in all_products:
                buying[item] = quantity 
                break  
    else:    
        buying[item] = quantity 
 
add = input('Want something else?(y/n): ').lower()

if add == "y":
    n = int(input('How many products you want to buy? :'))
    print('Name the items you want to buy:')
    for product in range(1, n+1):
        item = input(f'Item {product}:').capitalize()
        quantity = int(input('Quantity:'))
        if item not in all_products:
            while True:
                print(f'{item} is not available. Please enter a valid product.')
                item = input(f'Item {product}:').capitalize()
                quantity = int(input('Quantity:'))
                if item in all_products:
                    buying[item] = quantity 
                    break  
        else:    
            buying[item] = quantity 
 
 
print("Products you are buying:\n\n\tItems\tQuantity")    
for item, quantity in buying.items():
    print(f"\t{item} : {quantity}")

total = 0

for item, quantity in buying.items():
    total += (all_products[item]) * quantity 
     
if balance >= total:
    print(f'\nYour Total Amount is {total}₹\nYou can proceed to pay.')  
else:
    print(f"\nYour Total Amount is {total}₹\nInsufficient Card Balance.")









    