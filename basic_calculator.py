no1 = float(input("What is the first number? "))
no2 = float(input("What is the second number? "))
print("Please choose from 4 operations: add, subtract, multiply, divide. ")
operation = input("What is the operation? ")
if operation == "add":
    print(f"{no1} + {no2} = {no1+no2}")
elif operation == "subtract":
    print(f"{no1} - {no2} = {no1-no2}")
elif operation == "multiply":
    print(f"{no1} * {no2} = {no1*no2}")
elif operation == "divide":
    if no2 == 0:
        print("ERROR: cannot divide by zero!")
    else:
        print(f"{no1} / {no2} = {no1/no2}")
else:
    print("ERROR! Please type in a valid operator: add, subtract, multiply, divide!")
