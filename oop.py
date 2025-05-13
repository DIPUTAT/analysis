class Animal():
    legs = 4
    eyes = 2
    tall = True
    ears = 2
    teeths = True

    def eat(self):
        print("Фига как вкусно")

    def sleep(self):
        print("zzz")

    def walk(self):
        print("Гулять")

murzik = Animal()
bobik = Animal()
print(murzik.legs)
murzik.sleep()