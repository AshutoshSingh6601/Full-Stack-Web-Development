def login(User_name, Password):
    user_input = input("Enter User name :")
    user_pass = input("Enter User Pass :")
    if User_name == user_input and Password == user_pass:
        print("Right")
    elif User_name != user_input and Password == user_pass:
        print("Wrong User name ")
    elif User_name == user_input and Password != user_pass:
        print("Wrong password")
    else:
        print("Both are wrong")
login("abc", "xyz")