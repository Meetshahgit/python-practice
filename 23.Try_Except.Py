# This helps you catch error in Python
# Sometimes the code doesnt work or some line code might get executed due to which you might see an error

# Try except block 
try:
    number = int(input("enter a number: "))
    print(number)
except ValueError:
    print("invalid input")

# This help us protect our program from crashing so we dont get slammed with error 
# we have specify what type of error we wish to catch so that we dont end up catching all error under try

print ('we have created a calculator!!')

try:
    number = int(input(" enter a first number: "))
    number_2= int(input(" enter a second number: "))
    Operator = input("add a operator: ")
    
    if Operator == "+":
        sum = number + number_2
    elif Operator == "-":
        sum = number - number_2
    elif Operator  == "x" or Operator == "*":
        sum = number * number_2
    elif Operator == "/":
        sum = number / number_2
    else:
        print('invalid operation')
    print(sum)
except ValueError:
    print(" thats not a number !!")
except ZeroDivisionError:
    print(" you can perform that operation ")


