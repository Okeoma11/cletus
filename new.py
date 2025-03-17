# with open("information1.txt","r")as file:
#     content = file.read()
#     print(content)



# with open("information1.txt", "w") as file:
#     file.write("Hello, World!")
#     print("Content added successfully!!")

# lines =["First line\n", " Second line\n","Third line\n"]
# with open("information1.txt", "w") as file:
#     file.writelines(lines)
#     print("Content added Successfully!!")


# file = open("example.txt", "w")
# file.write("Hello, World!") 
# file.close()
# print ("file opened successfully!!")   

# file = open("example.txt", "a")
# file.write("Applending this./n")
# file.close()
# print ("File opened successfully!!")


# fo = open("foo.txt", "w+")
# fo.write("This is a elephant race")
# fo.seek(10,0)
# data = fo.read(3)
# fo.seek(10,0)
# fo.write('cat')
# fo.close()

import os

current_name = "information1.txt"
new_name = "newfile.txt"
os. rename(current_name, new_name)
print(f"file'{current_name}' renamed to '{new_name}' successfully.")
