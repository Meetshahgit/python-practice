# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# dictionary is usually created in curly brackets "{}"
# we will create a month conversions
# Jan -> Januray
# here is one eg:
monthConversions= {
    "Jan": "Janurary",
    "Feb": "Feburary",
    "Mar": "March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December", }

# We can get this by using print - this is mainly used when we have to refer similar slangs for the same word 

print(monthConversions["Nov"])
print(monthConversions["Mar"])

# we can also print in another using .get <- this function allows us to add a statement if the value is not found

print(monthConversions.get("Dec"))
# by default if the key is not assocaited we get an error: None
print(monthConversions.get("key","Not a Valid Key"))

# Dictonary can Contain Numbers instead of Strings

number_converstion= {
    0: "January",
    1: "Feburary",
    2: "March",
    3: "April",
    4: "May",
    5: "June",
    6: "July",
    7: "August",
    8: "Septemeber",
    9: "October",
    10: "November",
    11: "December",
}

print(number_converstion[1])
