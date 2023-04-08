class Cat:
    isHungry = True

    def __init__(self,name):
        self.name = name

    def play(self,person):
        print("In playing with", person.name)
        person.isHappy = True

class Person:
    isHappy = False

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def feed(self, cat):
        if cat.isHungry:
            print(self.name, "is feeding cat named", cat.name)
            cat.isHungry = False
        else:
            print(cat.name, "is not hungry")




my_cat = Cat("Barsik")
me = Person("Sasha", 13)
friend = Person("Vania", 14)
streat_cat = Cat("Olik")
me.feed(streat_cat)

me.feed(my_cat)
