class Mammal:
    def walk(self):
        print("walk")
    def bark(self):
        print("bark")


class Dog(Mammal):
    pass


class Cat(Mammal):
    def be_anooying(self):
        print("be annoying")

dog1=Dog()
dog1.walk()
dog1.bark()

cat1=Cat()
cat1.be_anooying()