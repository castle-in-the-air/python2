class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}.")


Roger = Person("Roger Federer")
print(Roger.name)
Roger.talk()

Owen= Person("Michael Owen")
Owen.talk()