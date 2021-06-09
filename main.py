# Slug Knights
# Win draw lose
#
#
#
#

import random as rand

print(
    """
    -----------------------
        SLUG KNIGHTS
    -----------------------
    """
)

attack_options = (
    "\nYour attack choices are:\n[1] Strike\n[2] Parry\n[3] Block\n[4] Heal"
)


class Character:
    def __init__(self, name, damage=30, slime=10, health=100):
        self.name = name
        self.damage = damage
        self.slime = slime
        self.health = health

    def __repr__(self):
        return f"Character({self.name}, {self.damage}, {self.slime}, {self.health})"

    def take_damage(self, dmg):
        self.health -= dmg

    def strike(self):
        print(f"{self.name} has striked.")
        self.slime -= 3
        return self.damage

    def parry(self):
        print(f"{self.name} has parried.")
        self.slime -= 4
        return self.damage * 1.5

    def block(self):
        print(f"{self.name} has blocked.")
        self.slime -= 2
        return 30

    def Heal(self):
        self.slime -= 3
        self.health += 30
        return self.health


def outcome(p1_choice, cp_choice):
    p1 = p1_choice
    cp = cp_choice

    if p1 == 1:
        if cp == 1:
            P1.take_damage(Cp.strike())


P1_name = input("What is your slugs name: ")
P1 = Character(P1_name)
Cp = Character("robot slug")

run = True

while run:

    if P1.slime <= 10:
        P1.slime += 2
        if P1.slime > 10:
            P1.slime = 10

    print(attack_options)
    p1_choice = int(input(f"What will you do {P1.name.title()}: "))
    cp_choice = 1

    outcome(p1_choice, cp_choice)

    if P1.health <= 0:
        run = False
        print("DEAD SLUG")

    print(P1.health)
    break
