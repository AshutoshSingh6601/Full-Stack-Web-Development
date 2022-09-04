str = ("happy new year Ashutosh")
char = '$'
vowels = 'aeiouAEIOU'
newstr = ""

for i in range(len(str)):
        if str[i] in vowels:
            newstr = newstr + char
        else:
            newstr = newstr + str[i]

# print(str)
print(newstr)