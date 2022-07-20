# Program to print  Multiplication table


# To take input from the user
number = int(input("Enter a number to display a table  "))

# 20 Iterations i.e j from 1 to 20
for j in range(1, 21):
   print(number, ' X ', j, ' = ', number*j)