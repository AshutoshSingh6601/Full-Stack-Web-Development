# Fibonacci series :- 0,1,1,2,3,5,8

num = int(input("Enter the number"))
count=0
n1, n2 = 0, 1
 
if num<=0:
    print("not enter a -ve Number")
elif num==1:
    print(f"fibonacci is {num}")

else:
    print("Fibonacci sequence")

while count<num:
    print(n1)
    nth = n1+n2
    n1=n2
    n2=nth
    count = count+1