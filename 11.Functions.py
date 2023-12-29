
## Python has function which you can create 
# a Function needs to have a name
# the code has to be indented
def say_hi ():
    print("Hello User")

# Once the function is created we need to call that function in order to use the function
say_hi()


## sample function example
shop_list = []

def shopping ():
    i = input("add an Item: ")
    shop_list.append(i)

shopping()
print(shop_list)

## you can function powerful by adding parameters

def say_hi(name):
    print("hello "+ name)

say_hi("Lenovo")
say_hi("Dell")

## you can have more than 1 parameter

def say_hi (name,age):
    print("hello "+ name)
    print("you are " + str(age) + " years old.")

say_hi("Messi", 37)
say_hi("Ronaldo", 38)