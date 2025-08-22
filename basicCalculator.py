#Basic Calculator Program
num1 = float(input("Enter The First Number: "))
num2 = float(input("Enter The Second Number: "))

operators = input("Enter the operation (+, -, *, /) ")

if operators == "+":
    results = num1 + num2
    print(f"{num1} + {num2} = {results}")
    
elif operators == "-":
    results = num1 - num2
    print(f"{num1} - {num2} = {results}")
    
elif operators == "*":
    results = num1 * num2
    print(f"{num1} * {num2} = {results}")
    
elif operators == "/":
    if num2 != 0: #To prevent the numbers to be divided by 0
     results = num1 / num2
     print(f"{num1} + {num2} = {results}")
    else:
         print("Cannot be divided by 0")

else:
    print("Invalid Operations")         