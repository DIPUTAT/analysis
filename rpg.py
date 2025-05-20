class People():
    hp = 100
    dmg = 10
    armor = 2
    regen = 2

    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        enemy.hp -= self.dmg // enemy.armor

    def hi(self):
        self.hp += self.regen



obj1 = People("Ромапро2000")
obj2 = People("Арсенийпро2010")

print(obj2.hp)
obj1.attack(obj2)
obj2.hi()
print(obj2.hp)



