"""Question 1"""
out_file = open("name.txt", "w")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()
#
"""Question 2"""
in_file = open("name.txt", "r")
print(in_file.read())
in_file.close()

"""Question 2.5"""
with open("name.txt", "r") as in_file:
    name = in_file.read().strip()
print("Your name is", name)

"""Question 3"""
number_file = open("numbers.txt", "r")
number_line = 0
line = number_file.readline()
for line in number_file:
    number_line += 1
    print(line)
number_file.close()
