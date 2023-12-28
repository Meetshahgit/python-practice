## Python allows you to create list
# List is used to when we have more than one varible to work on
# to create list we use [] these brackets

list_of_person_i_know = ["Bookkie","Lesile","Cammron","Anne","James", "Grant","Jeff","Ponzi"]
print(list_of_person_i_know)

# list can contain any item of things like number, names, decimal, boolean etc....
# list can also be mix between 2 or more variable variable

list = [2,"maths",5,False]

# you can acces indivdual items in a list using there index (by default index starts at '0') 
# you can access individual item using [place there index number over here]
print(list_of_person_i_know[2])

# you also index with negetive index like -1 , -2 , - 3 .... and so On . negetive index start the list from other side
# negetive index starts at -1 and not - 0 (hehehe that doesnt exist)
print(list_of_person_i_know[-1])

## Python also allows you to select a values from anywhere after the index mention ':'
print(list_of_person_i_know[3:])
print(list_of_person_i_know[-3:])

# Python also lets to select a range from list instead of selecting the whole list
print(list_of_person_i_know[4:6])

# you can modify or replace list value using = 
list_of_person_i_know[-1] = "Dash"
print(list_of_person_i_know[-1])