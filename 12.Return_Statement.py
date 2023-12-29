
# Return function allows Python to return information how a code is executed
## return works along with Define function statement
def cube(num):
    pow(num,3)

cube(4)
# while printing this function we get an message saying "None";

print(cube(4))

# To get any value from this function we use return

def cube(num):
    return pow(num,3)

print(cube(4))

# you can put any additional code in function after return function

def run(num):
    return num*5
    print(" your dumb")

result = run(4)
print(result)

# Here you can see it skipped on the print command after return function,
# PS D:\personal project\python practice> & C:/Users/manns/AppData/Local/Microsoft/WindowsApps/python3.11.exe "d:/personal project/python practice/12.Return_Statement.py"
# None
# 64
# 20

## if we want to see this print statement then we would have to type this either above return or on new line (not in Def)

def run(num):
    print(" your dumb")
    return num*5


result = run(4)
print(result)

## Return also act as an break function, Since it is a tail function where code ends.
