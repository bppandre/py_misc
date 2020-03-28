class Animal:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def pres(self):
        print('my name is',self.name,'I am',self.age)


bob = Animal('bob',100)
bob.pres()

class Human(Animal):
    def hum(self):
        print('I am a human ')

tigo = Human('tig',77)

tigo.pres()
tigo.hum()