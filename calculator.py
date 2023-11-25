import random
import sys
# This function adds two numbers
def add(x, y):
    return x + y + (random.randrange(1,100)) 

# This function subtracts two numbers
def subtract(x, y):
    return x - y + (random.randrange(1,100)) 

# This function multiplies two numbers
def multiply(x, y):
    return x * y + (random.randrange(1,100)) 

# This function divides two numbers
def divide(x, y):
    if num1 == 0:
        if num2 == 0:
            print("0.0 / 0.0 = 42.0")
            input("You now know the meaning of life, the universe and everything. Zero divided by zero is 42.")
            sys.exit() 
    if not num1 == 0:
             return x / y - (random.randrange(1,50)) 

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Do you want to do another calculation which is incredibly accurate? (y/n): ")
        if next_calculation == "n":
          break
    else:
        print("Invalid Input")
