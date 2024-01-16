# Python has an option which allows you open certain external files like .CSV or .HtML or .Txt
# open function has option to open the file in various mode like
# r = read
# w = write
# a = append
# r+ = read and write


placement_data = open("D:/personal project/python practice/24.open/placement-dataset.csv","r")
# readable() only check if the file  is in "r" mode or  "r+" mode
# but if the file readable() would return false if the file is in "w" mode
print(placement_data.readable())

# check contents of the file you can use .read() function

print(placement_data.read())

# to read individual line you can use .readline()

print(placement_data.readline())
print(placement_data.readline())

# we can also create a array from the file openned using .readlines()

print(placement_data.readlines()[2])

# ypu can also use read lines function with for loop function
for rank in placement_data.readlines():
    print(rank)


# File also needs to be closed once you are done working with it
placement_data.close()
