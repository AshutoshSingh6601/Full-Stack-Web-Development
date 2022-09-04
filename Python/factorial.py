list1 = [5, 4, 3, 2, 1]
list2 = []
factorial = 1

for i in list1:
    for j in range(1, i+1):
        factorial = factorial*j
    list2.append(factorial)
    factorial = 1
print(list2)