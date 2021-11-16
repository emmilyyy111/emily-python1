# name = input("Enter your name: ")
# age = input("Enter your age: ")
#
# print("Hello " + name + ", you are " + age + " years old")
#

# opening and reading a file "r" - get
# open("employees.txt", "r")
#
# # opening and writing or changing a file "w" - update
# open("employees.txt", "w")
#
# # append/ add new info to the end of the file, cant modify but can add "a"
# open("employees.txt", "a")
#
# # read and write permissions "r+"
# open("employees.txt", "r+")

# getting all of the lines in the file
# employee_file = open("employees.txt", "r")
# for employee in employee_file.readlines():
#     print(employee)
#
# employee_file.close()

# adding to the end of the file
employee_file = open("index.html", "w")
employee_file.write("<h1> Hi Emily ! </h1>")
# print(employee_file.read())

employee_file.close()




