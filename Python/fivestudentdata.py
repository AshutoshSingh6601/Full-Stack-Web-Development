from posixpath import split


count=0
list1 = []
while count<5:
    class student:
        def __init__(self, id, name, marks):
            self.id = id
            self.name = name
            self.marks = marks
        def display(self):
            print(f'{self.id}, {self.name}, {self.marks}')
    userData = input("Enter your id, name, marks: ")
    
    list1.append(userData)
    print(list1)
    count=count+1