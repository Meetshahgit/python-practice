# Python has a function which allows you take a number and raise to a specific power
# there is a really easy way to do this

# ** is power 
print(2**3) # this is 2^3

# we can also create exponent function using for loops

def raise_to_power(base_num,pow_num):
# since we dont know what input we will recieve for pow_num 
    result = 1 
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3,2))

# This function is an example of how loops works
# here the we take 2 number in our function raise_to_power and then multiple the base_num by itself in loop sequence create in for loop