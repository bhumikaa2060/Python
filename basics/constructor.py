class Person:
    def __init__(self, name): #attribute
        self.name= name
    def talk(self): #method
        print(f"Hi, I am {self.name}")


class studet(Person):  #inheritance
    pass

Person1 = Person('Bhumika')
Person1.talk()
student = studet("bhm")

student.talk()
print(Person1.name)