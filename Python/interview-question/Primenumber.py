# Prime number = divisible by 1 or itself

num = 29
valid= False
if num>1:
    for i in range(2, num):
        if (num%i)==0:
            valid=True 
            break
if valid:
    print(f"{num} is not a Prime number")
else:
    print(f"{num} it's a Prime number")