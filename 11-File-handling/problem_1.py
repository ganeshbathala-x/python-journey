#1 we need to close file
file =open("games.txt","r")

content =file.read()
print(content)
file.close()
#2 automatically file closed
with open("games.txt","r") as file:
    content =file.read()
    print(content)

#3 for read only one line in file
with open("games.txt","r") as file:
    print(file.readline())

#4 for read all lines as list
with open("games.txt","r") as file:
    print(file.readlines())

#5foroverwrites the existing content
with open("games.txt","w") as file:
    file.write("valorant\n")
    file.write("mine craft\n")

#for add a new content into file without deliting existing content
with open("games.txt","a") as file:
    file.write("temple run\n")
#7 for print the current cursor
with open("games.txt","r") as file:
    print(file.read(2))
    print(file.tell())
#8 move the cursor to specific postion
with open("games.txt","r") as file:
    print(file.read(3))
    print(file.tell())
    print(file.seek(0))
    