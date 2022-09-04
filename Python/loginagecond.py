username = "abc"
password = "xyz"
user_enter = input("Enter Username")
password_enter = input("Enter Password")

if username == user_enter and password == password_enter:
    print("success")
elif username == user_enter and password != password_enter:
    print("invalid pass")
elif username != user_enter and password == password_enter:
    print("invalid user")  
else:
    print("Both invalid ")  