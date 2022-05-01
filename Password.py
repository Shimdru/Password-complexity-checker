import re
p= input("Input your password: ")
x = True
while x:  
    if len(p) < 8:
        print("Make sure your password is at lest 8 letters")
        break
    elif not re.search("[a-z]",p):
        print("Make sure your password is at least a lower case letter")
        break
    elif not re.search("[0-9]",p):
        print("Make sure your password has a number in it")
        break
    elif not re.search("[A-Z]",p):
        print("Make sure your password is at least a upper case letter")
        break
    elif not re.search("[$#@!&]",p):
        print("Make sure your password is at least one of the following special characters $ # @ ! &")
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break