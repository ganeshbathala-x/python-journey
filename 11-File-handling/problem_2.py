try:
    with open("unknown.txt","r") as file:
        print(file.read())

except FileNotFoundError as e:
    print ("file not found",e)
else:
    print("file readed successfully")
finally:
    print("operation completed")
