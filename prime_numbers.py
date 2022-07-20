# Program to print prime numbers between 1 to 100

# To take input from the user
#num = int(input("Enter a number: "))




flag = False

# number range from 2 to 100
for  num in range(2, 100) :
    flag = False
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if  (flag == False):
        print(num)
