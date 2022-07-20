# This program read a numbers prints square root of that number with cmath module
import cmath

# for complex numbers we have to use eval funcinon to convert complex numbers (5+2j) string to complex number
number = eval(input('Enter a number: '))

# sqrt of a number
sqrt = cmath.sqrt(number)

# Display the sqrt
print('square root of ',number, " is ", sqrt)
