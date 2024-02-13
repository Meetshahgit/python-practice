# Classes and Objects help you make your program more organised and  more powerfull

# when working on Python we work with lots of data
    # We mainly work these type of data the most
            # String 
            # Boolean
            # Int/Float
# Classes and object means we can create our own data types

# we can start by saying class
class my_watch:
    
    def __init__(self, Name, year, in_production):
        self.Name = Name
        self.year = year
        self.in_production = in_production 

# A Class is a blueprint for creating objects

watch1 = my_watch("Casio",2002,False)
watch2= my_watch("Samsung watch 4",2021,True)
print(watch1.Name)
print(watch2.in_production)

# Now you can uses these classes along with other code