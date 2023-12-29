## Python allows to print numbers with intverted comas
print(2)

## print also alows you to print decimel and negetive numbers too
print(2.543453)
print(-65.212)

## Python has built in arthimetic functions like addition (+), subtraction(-), dividtion(/), multiplication (*)
print(3 + 5)
print(4*5)
print(12/4)
print(20 - 12)

## python performs arthimetric operation from left to right by default you can change the pirority of the arthimetric operation using brackets
print(4*(3 + 5))

## Python also has option to use % sign to get the remainder in a dividion operation - % (modulus Operator)
print(10 % 3)
print(10 / 3)

## Python also the number to assigned to any variable
my_num = 5
print(my_num)

## Python also you to convert number into string
print(str(my_num) + " My favourite number")

## if you dont convert to str and run the same operator it will spit out an error
print(my_num + " My favourite number")

## Some of the most commonly used Operator are 

    ## 1. ABS (absolute value)
my_num = -24.4
print(abs(my_num))
    ## this value removes any negetive integer making it positive

    ## 2. pow() this functions allows you to get a power of any number 
print(pow(3,3))

    ## 3. max() returns the maximum value from the numbers given
print(max(12,5))
    ## 4. min() returns with the lowest value from the given number
print(min(12,5))
    ## 5. round () this function will round any value to the nearest 0
print(round(12.53))

### Python allows you to import external code into our library
from math import *

    ## 6. Floor() turns any decimel into whole number (doesnt round or change only removes the decimel)
print(floor(4.445))
    ## 7. Ceil () it will round the number to nearest next number
print(ceil(4.3))
    ## 8 . Sqrt() it will return with the squareroot of any number
print(sqrt(12))