# Python has an option which allows you open certain external files like .CSV or .HtML or .Txt
#  we can add and append data on to an existing file

# we can check the file and it content 
placement_data = open("D:/personal project/python practice/24.open/placement-dataset.csv","r")
print(placement_data.read())
placement_data.close()

# so append adds data on to the file at end of file 
placement_data = open("D:/personal project/python practice/24.open/placement-dataset.csv","a")

# to insert line at the end of the file or write data on the file we use .write()

# placement_data.write("101,4.3,120.0,1")

# Python doesnt auto push data on the new line while inserting data we add "\n"
# placement_data.write("\n101,4.3,150.0,0")
placement_data.close()

# when we use "w" it will overwite on an existing file contents of that file will be lost
# be carefull when using "w"
# "w"  can be used to create a new file

new_file = open("learning.HTML","w")
new_file.write(" <!DOCTYPE html><html><head><title>Hi I am learning python</title></head><body<h1>Hi I am learning python</h1></body></html>")