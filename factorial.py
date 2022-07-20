# This program contains two python funcions to find of a factorial of a number



#  1. function to findout factorial out recurstion.
def simple_factorial(number):
    fac = 1
    for j in range(1, number + 1):
       fac = fac*j
    return fac


#  2. recursive function to find out factorial. 
def rec_factorial(f):
    """This is a recursive function
    to find the factorial of an integer"""

    if f == 1:
        return 1
    else:
        # recursive call to the function
        return (f * rec_factorial(f-1))



# to take input from the user
number = int(input("Enter a number to find out factorial: "))

if number < 0:
   print("Factorial does not exist for negative numbers")
   quit()
elif number == 0:
   print("The factorial of 0 is 1")
   quit()

#  simple factorial function call
factorial = simple_factorial(number)
print("The factorial of", number, "by using simple factorial fucntion is", factorial)

#  recursive factorial function call
factorial = rec_factorial(number)
print("The factorial of", number, "by using recursive factorial fucntion is", factorial)