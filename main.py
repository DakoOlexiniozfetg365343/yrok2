class Cat:
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


my_cat = Cat("Barsik")
me = Person("Sasha", 13)
friend = Person("Vania", 14)

print(me.isHappy)

my_cat.play(me)
my_cat.play(friend)

print(me.isHappy)
