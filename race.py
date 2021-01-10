from datetime import datetime, timedelta


class Human:

    def __init__(self, title, hp, stamina, speed, level, attack, reload):
        self.title = title
        self.hp = hp
        self.stamina = stamina
        self.speed = speed
        self.level = level
        self.attack = attack
        self.reload_time = reload
        self.last_attack = None

    def check_attack(self):
        if self.last_attack and datetime.now()-self.last_attack < timedelta(microseconds=self.reload_time):
            return False
        else:
            return True

    def attack_func(self):
        if self.check_attack():
            self.last_attack = datetime.now()
            print("boom")
            return self.attack
        else:
            print("Pls, wait!")
            return 0

    def __str__(self):
        return f"Race: {self.title}"


class Archer(Human):
    def __init__(self, level):
        self.title = "Archer"
        super().__init__(self.title,
                         80 + level*20,
                         95 + level*5,
                         3,
                         level,
                         35+level*5,
                         120
                         )


class Knight(Human):
    def __init__(self, level):
        self.title = "Knight"
        super().__init__(self.title,
                         130 + level*20,
                         85 + level*5,
                         1,
                         level,
                         55+level*5,
                         130
                         )


class Wizard(Human):
    def __init__(self, level):
        self.title = "Wizard"
        super().__init__(self.title,
                         80 + level*10,
                         105 + level*10,
                         5,
                         level,
                         45+level*15,
                         110
                         )
