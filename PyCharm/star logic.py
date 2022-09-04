# Take input from User
n=int(input('Enter the number'))#n=5
# i can initilazed 0 to n-1 i.e i=0 to n-1
for i in range(0, n):
    # j can initilazed 0 tak jayega i ke value se
     for j in range(0, i+1):
        # print karega * ke value ko aur end=" " ye print karega space
        print("*", end=" ")
        # \r is same like new line
     print("\r")