def pelindrome(name):
    list1 = name
    list2 = list1[::-1]
    if list1 == list2:
        print("Palindrome")
    else:
        print("not Pelindrome")
pelindrome("Ashutosh")