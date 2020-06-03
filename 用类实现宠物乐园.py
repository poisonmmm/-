class Animal():
    def __init__(self, nickname, type, age, relation=50, health=50):
        self.nickname = nickname
        self.type = type
        self.age = age
        self.relation = relation
        self.health = health

    def play(self):
        self.relation += 10
        self.health -= 15
        print(self.nickname, "的健康值是%d，亲密度是%d" % (self.health, self.relation))

    def eat(self):
        self.relation -= 5
        self.health += 10
        print(self.nickname, "的健康值是%d，亲密度是%d" % (self.health, self.relation))


class people():
    def __init__(self, name):
        self.name = name

    def feed_Animal(self, Animal):
        Animal.eat()

    def play_Animal(self, Animal):
        Animal.play()


cat = Animal("小花", "花猫", 3)
dog = Animal("汪汪", "哈士奇", 3)
master = people("小明")
master.feed_Animal(cat)
