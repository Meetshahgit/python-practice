## Now we we will create a calcalutor which will work much better that our current one
# this will allow user to more than just addtion

num1 = float(input("Enter First number: "))
operator = input("Enter Operator:")
num2 = float(input("Enter Second number: "))

if operator == "+" or operator == "Additon" or operator == "add":
    print(num1 + num2)
elif operator == "-" or operator == "Subtraction" or operator == "minus":
    print(num1 - num2)
elif operator == "x" or operator == "*" or operator == "multiply":
    print(num1 * num2)
elif operator == "/" or operator == "Divide":
    print(num1/num2)
else:
    print("Invalid Operator")