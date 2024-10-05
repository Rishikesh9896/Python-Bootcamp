number = input("Enter the character")
ascii = ord(number)
if(ascii>=97 and ascii<=122):
    print("It is a lower case alphabet")
elif(ascii>=65 and ascii<=90):
    print("Its a upper case alphabet")
else:
    print("Its not a character")