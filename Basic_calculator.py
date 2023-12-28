## Basic Calculator
## this a simple application which compiles all the things we have learned so far

## we will take 2 numbers from user and add both numbers
## we will store 1st number in num1
num1 = input("enter any number:")
## we will store the second number in num2
num2 = input("enter another number:")

## addition of both number will be in answer
## by default user input are consider as string and not number we add int(for whole number) & if we want to add decimal numbers then float()
## this ensures that Python take user input as value instead of letters
answer = float(num1) + float(num2)

## this will print out the answer with a nice string
print("we have added both number for you " + str(answer) +" is your answer" )

## this calculator only adds 2 number it can be whole number or decimal
