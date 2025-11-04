class Dog:
    def __init__(self):
        self.name=Name
        self.bread=bread

    def bark(self):
        return f"{self.name} says woof"


dog=Dog("max","lara")
print(dog.bark())

print("dog",dog.bread)

with open("exs.txt","w") as file:
    file.write("this is a sample ")
    file.write("second")

with open("exs.txt","r") as file:
   content=file.read()
print("file content",content)




try:
    result=10/0
except ZeroDivisionError:
    print("error division by zero")


squr=[x**2 for x in range(1,6)]
print("squares",squr)

cube=lambda x:x**3
print("dc",cube(3))





        
