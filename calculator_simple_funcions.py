# A simple calculator implementation using python functions


# division funciton
def divide(p, q):
    return p / q
# add function
def add(p, q):
    return p + q

# substratct function
def subtract(p, q):
    return p - q

# multiplication function 
def multiply(p, q):
    return p * q


while True:
    # take input from the user
    choice = input(" 1.Add \n 2.Subtract \n 3.Multiplay \n 4.Divide \n 5.quit \n Enter choice(1/2/3/4/5): ")

    # check if selection is one of the four options
    if choice in ('1', '2', '3', '4'):
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        if choice == '1':
            print(number1, "+", number2, "=", add(number1, number2))

        elif choice == '2':
            print(number1, "-", number2, "=", subtract(number1, number2))

        elif choice == '3':
            print(number1, "*", number2, "=", multiply(number1, number2))

        elif choice == '4':
            print(number1, "/", number2, "=", divide(number1, number2))        
   
    elif choice == '5':
        print('Thank you for using python simple calculator')
        break
    
    else :
        print("Invalid Input")