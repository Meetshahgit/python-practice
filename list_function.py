## this list and its functions that you can perform with a list

appointment_time = [7,9,11,12,13,15,20,23]
appointment_days = ["Monday","Tuesday","wednesday","Thrusday","Friday","Saturday"]

## you can print list
print(appointment_days)

## Python allows you to combine 2 or more list using .extend functions
appointment_days.extend(appointment_time)
print(appointment_days)

## you can add items to your existing list using .append function it will add a item at the end of the list

appointment_days = ["Monday","Tuesday","wednesday","Thrusday","Friday","Saturday"]
appointment_days.append("Sunday")
print(appointment_days)

## if want to add item between 2 items you can use insert function .insert(index, value/string)
appointment_time.insert(7,21)
print(appointment_time)

## Python also allows you to remove elements from the list with .remove function 
appointment_days.remove("Sunday")
print(appointment_days)

## Python also allows to clear the list using .Clear()
appointment_days.clear()
print(appointment_days)

## Python has this function call Pop() this functions removes the last time from the list
appointment_days = ["Monday","Tuesday","wednesday","Thrusday","Friday","Saturday"]
appointment_days.pop()
print(appointment_days)

## Python has a option which lets you search a certain list using .index() it will return with index number

print(appointment_days.index("wednesday"))
# if a certain item is not on the list then it will show an error

# print(appointment_time.index(5))
#Traceback (most recent call last):
#   File "d:\personal project\python practice\list_function.py", line 41, in <module>
#     print(appointment_time.index(5))
#           ^^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: 5 is not in list

## .count function is used to check how many times a value or variable has been repeated in the list
i = ["I","Love","Love","Love","Python","I","Python"]
print(i.count("Love"))


## to sort the list you can use .sort function 
# it can sort list in accending order or decending order either aphabetical order or from low to high value
appointment_time.sort()
print(appointment_time)

## you can reverse the list with reverse function
appointment_time.reverse()
print(appointment_time)

## you can copy a list with .copy function

new_year_appointment = appointment_time.copy()
print(new_year_appointment)