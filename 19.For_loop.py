## A for loop is a way of iterating over a sequence of items, such as a list, a tuple, a string, or a range
# The syntax of a for loop is: for variable in sequence: do something\

# for letter in "Learning Python":
#     print(letter)

# For Loop can also be used in a Array
    
friends = ["Tony","Martina","Paula","Chetan"]
for friend in friends:
    print(friend)

print("new loop")

# you can also loop through number 
    
for Index in range(10):
    print(Index)
print("Done!!")
# you also specify a start and end in range while looping

for number in range(3,10):
    print(number)
print("new loop ")
# you can also pass array in range while looping in for loops

friends = ["Asha","Dell","Sever","Sam"]
for Index in range(len(friends)):
    print(friends[Index])

# if we want to loop through one name in the friends list 
# this loop will only loop for friend with index number 2 ie sever for the duration of the whole loop
# since this loop has 4 names it will print the name 4 times.

friends = ["Asha","Dell","Sever","Sam"]
for Index in range(len(friends)):
    print(friends[2])

# you can any logic in for loops 

for index in range (5):
    if index == 0:
        print("first itteration")
    else:
        print("not first")