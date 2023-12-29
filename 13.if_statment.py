## If are one the most commonly used function in Python
# IF statement allows Python to perform task based on parameters given

# eg of If statement

# I wake up
#   if I am late
#   then I get dressed and leave
# else I eat my breakfast too and leave

# IF statment is is also like def(function) 

not_hungry = True
if not_hungry:
    print("then Work on your code")
# If statment can work with 1 or more parameters
# by default we use 2 parameter in 
else:
    print("Go eat food")

## New If statment
    
## this IF statment combines 2 parameters

are_you_hungry = False
Crave_sweet = False

if Crave_sweet:
    print("Lets go for Icecream or Pancakes?")
elif are_you_hungry:
    print("lets go for Lunch or Dinner?")
else:
    print("your not hungry")

## Now lets combine if statement with  OR


if Crave_sweet or are_you_hungry:
    print("you are hunry and you crave sweet? or your Just craving sweet and not hungry ?")
else:
    print("you dont want to have food!")

## Now lets tweak this Statment with AND operator

food = True
sweet = False
if food and sweet:
    print("you need to go out and eat food!! Dont forget Desserts!!!")
elif food:
    print("you need Food!!")
elif sweet:
    print("you are craving something sweet!!")
else:
    print("you need to have food please continue working on your code!!")

# you can use "and not" 

are_you_hungry = True
Crave_sweet = True

if are_you_hungry and Crave_sweet:
    print("you are hungry and crave sweet")
elif not(are_you_hungry) and Crave_sweet:
    print("you just want something sweet!!")
elif are_you_hungry and not(Crave_sweet):
    print("your hungry you, order something now!!")
else:
    print("get back to work")
