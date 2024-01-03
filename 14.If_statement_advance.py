# we can use If statment for comparision 
# we will create function 

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return print(str(num1) + " is larger")
    elif num2 >= num1 and num2 >= num3:
        return print(str(num2) + "is Larger")
    else:
        return print(str(num3) + " is larger")

max_num(29,39,100)

# Python also lets you compare 2 non numeric operations
def animal_name(animal1, animal2):
    if animal1.lower() == "poodle":
        return print("Best breed ever")
    elif animal1.lower() == "bulldog":
        return print("Beauty meets loyal")
    else:
        return print("You are an idiot")

animal_name('Poodle', 'Bulldog')

# one of the most common is '==' , '!=', '<=' , '>=' 