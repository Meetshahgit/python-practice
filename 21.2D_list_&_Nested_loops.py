## Python allows you to create grid like patten which where a list is divided into individual list, 
# Python allows allows you retrive individual items in those list

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

# if you want to access any of the values in the grid
print(number_grid [0][0])
# if you see this print statement you will see that we 2 parameters first [] specify the outer rows index and [] specify inter list index

friends_grid = [
    ["Parth","Alen","Tony","Frank"],
    ["Michel","trevor","Lamar","Alex"],
    ["Vence","Paris","Preethi","jithin"],
    ["Gandhi","Modi","Mike","Goat"]
]

print(friends_grid[2][1])


## Nested For loops is a loop inside a loop
for row in number_grid:
    for col in row:
        print(col)

