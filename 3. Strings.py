print("Girafee Acedamy")

## backslas "\" is used as an escape charcter when paired with any of the following 
## if printed allow it will be part of the text
print("Happy\gorrila")

## \n creates new line in print statment
print("Water \n Slide")

## \" allows you add quotation mark to the print statment
print(" \"PHP\" & \"MySQL\" for dummies")

## python lets you print assigned strings using print function
pharse = "Mann Shah"
print(pharse)

## python lets you concate 2 or more strings or with an sentence using "+" Operator
pharse = "Mann shah"
pharse_2 = "He is 5 mins elder to me"
print(pharse + "is my elder brother."+ pharse_2)
print(pharse + ". "+ pharse_2)

## you can add functions to your strings by adding a "." after
## .lower() is for lowercase
print(pharse_2.lower())

## .upper() is for uppercase
print(pharse.upper())

## Python also lets you check for cases value retrived are in True or False
## .isupper()
print(pharse.isupper())

## .isLower()
print(pharse_2.islower())

## you can also combine 2 or more functions 
eg = "HE RIDES WITH ME DAILY"
print(eg.lower().islower())

## to count letter in a string use function len()
print(len(eg))

## using [] you can take each letter from the string

print(eg[5])

## Python allows you to index or to check where a character might be located in a given pharse. The function is .Index()
eg = "Learning Python so that you can focus on other things in Life"
print(eg.index("i"))

## Python also allows you to index full words it will show where does the word start froms
eg = "Learning Python so that you can focus on other things in Life"
print(eg.index("other"))

## .replace allows to you to replace words 
eg = "Learning Python so that you can focus on other things in Life"
print(eg.replace("Python","SQL"))
