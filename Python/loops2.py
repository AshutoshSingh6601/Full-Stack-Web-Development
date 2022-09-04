list1=["Ashutosh", "Rohit", 10, 15.5, 15, 19, 20.5, 20]
list2=[]
list3=[]
list4=[]
for element in list1:
    if type(element) == str :
        list2.append(element)
    elif type(element) == float :
        list3.append(element)
    elif type(element) == int :
        list4.append(element)
print(list3)
print(list2)
print(list4)
