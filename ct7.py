import random

class Fighter:
    def __init__(self, name, height=None, weight=None):
        self.name = name
        self.height = height if height else random.randint(160, 200)
        self.weight = weight if weight else random.randint(60, 100)
        self.power = self.calculate_power()
        self.is_alive = True

    def calculate_power(self):
        bmi = self.weight / ((self.height / 100) ** 2)
        return int(bmi * 3)

    def attack(self, opponent):
        if opponent.is_alive:
            attack_strength = random.randint(5, 20)
            if random.random() < 0.5:
                print(f"{self.name} атакует {opponent.name} с силой {attack_strength}")
                opponent.take_damage(attack_strength)
                return True
            else:
                print(f"{self.name} попытался атаковать {opponent.name}, но {opponent.name} заблокировал удар")
        return False

    def take_damage(self, damage):
        self.power -= damage
        if self.power <= 0:
            self.is_alive = False
            print(f"{self.name} выбывает из поединка")

    def show_info(self):
        print(f"{self.name}: Рост: {self.height}, Вес: {self.weight}, Сила: {self.power}")

class Contest:
    def __init__(self, first, second):
        self.fighters = [first, second]
        random.shuffle(self.fighters)
        self.winner = None

    def fight(self):
        print("Поединок начинается!")
        print("-------------")
        self.fighters[0].show_info()
        self.fighters[1].show_info()
        print("-------------")

        while all(fighter.is_alive for fighter in self.fighters):
            for i in range(2):
                attacker = self.fighters[i]
                opponent = self.fighters[1 - i]
                if attacker.attack(opponent):
                    if not opponent.is_alive:
                        self.winner = attacker
                        break

        if self.winner:
            print("-------------")
            print(f"Победил боец {self.winner.name}")
        return self.winner

# Пример использования:
vasya = Fighter("Вася")
petya = Fighter("Петя")
contest = Contest(vasya, petya)
winner = contest.fight()
if winner:
    print("Победил боец", winner.name)