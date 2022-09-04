# factorial number = 5! i.e 5*4*3*2*1

num = 5
fact=1
if num<0:
    print("number not in -ve")
elif num==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print(fact)