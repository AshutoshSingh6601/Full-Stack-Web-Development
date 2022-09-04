from secrets import choice


dict1 = {
    'name':'ashutosh',
    'id':101,
    'salary':120,
    'company':'zeetech'
}
key=''
value=None
# print(dict1)
choice=int(input('If you looking for key click 1 and for value click 2: '))
if choice==1:
    key=input('Enter any key to find the value: ')
elif choice==2:
    value=input('Enter any value to find the key: ')
for x,y in dict1.items():
    z=str(y)
    if x==key:
        print(y)
    elif z==value:
        print(x)