class Animal():
    legs = 4
    eyes = 2
    tall = True
    ears = 2
    teeths = True

    def __init__ (self, name, age):
        print("Я крутой")
        self.name = name
        self.age = age

    def eat(self):
        print("Фига как вкусно")

    def sleep(self):
        print("zzz")

    def walk(self):
        print("Гуляю")

murzik = Animal("Мурзик", 52)
bobik = Animal("Бобик", 89)


class People(Animal):
    legs = 2
    def work(self):
        print("ВЫХООООДНОЙ")

    def sleep(self):
        print("Я не фигней занимаюсь")

dusha = People("Дюша", 17)
print(dusha.legs)


