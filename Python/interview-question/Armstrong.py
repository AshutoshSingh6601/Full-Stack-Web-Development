# Armstrong number = 153 i.e 1*1*1+5*5*5+3*3*3

num = 153
sum=0
order = len(str(num))
copy_num = num
while(num>0):
    digit=num%10
    sum +=digit**order
    num=num//10

if (sum==copy_num):
    print("it's a armstrong number")
else:
    print("It's not a armstrong number")
