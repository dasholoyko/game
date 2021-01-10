from personages.race import Archer, Knight, Wizard
print("bla bla ")
name = input("Enter hero's name: ")
ans = 0
while ans not in [1, 2, 3]:
    ans = int(input("Choose role(1: Archer, 2: Knight, 3: Wizard): "))
    if ans == 1:
        hero = Archer(1)
    elif ans == 2:
        hero = Knight(1)
    elif ans == 3:
        hero = Wizard(1)
    else:
        print("Error! Try again")
print(hero)

en1 = Knight(1)
print(en1.hp)

while en1.hp > 0 and hero.hp > 0:
    en1.hp -= hero.attack_func()
    if en1.hp > 0:
        hero.hp -= en1.attack_func()

if en1.hp <= 0:
    print(f"You win! your hp: {hero.hp}")
else:
    print(f"You lose! enemy's hp: {en1.hp}")
