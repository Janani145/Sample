
#FUNCTIONS TO PERFORM ARITHMETIC OPERATIONS
def addition(x, y):
    return x + y 

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y                

print("\n\t\t\tWELCOME TO THE CALCULATOR !!")

while True:
    print("\n\tSelect the operations:")
    print("1. Addition ")
    print("2. Subtraction ")
    print("3. Multiplication ")

    print("4. Division ")
    print("5. Exit")

    choice = input("Enter operation choice (1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", addition(num1, num2))
        elif choice == '2':
            print("Result:", subtraction(num1, num2))
        elif choice == '3':
            print("Result:", multiplication(num1, num2))
        elif choice == '4':
            print("Result:", division(num1, num2))
    elif choice == '5':
        print("Bye!")
        break
    else:
        print("Invalid input! Please enter a valid  choice.")
  #FUNCTIONS TO PERFORM ARITHMETIC OPERATIONS
def addition(x, y):
    return x + y 

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y                
