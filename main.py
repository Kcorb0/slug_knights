import random as rand
import os
from character import Character


def outcome(player, computer, p1_choice, cp_choice):
    # Takes the choices of the player and computer
    # Changes the player and computer objects

    p1 = p1_choice
    cp = cp_choice

    if p1 == 1:
        if cp == 1:
            player.take_damage(computer.strike())
        elif cp == 2:
            player.take_damage(computer.parry())
        elif cp == 3:
            pass


def slime_levels(player):
    # Controls the slime levels so they increment by 2 each round
    # But do not exceed 10

    if player.slime <= 10:
        player.slime += 2
        if player.slime > 10:
            player.slime = 10


title_card = """
    -----------------------
         SLUG KNIGHTS
    -----------------------
    """

print(title_card)
P1_name = input("What is your slugs name: ").title()
P1 = Character(P1_name)
Cp = Character("Slugtron")

run = True
round_num = 1

while run:

    # Print round number and increase round num by 1
    print(f"====== Round {round_num} ======")
    round_num += 1

    # Check slime levels
    slime_levels(P1)
    slime_levels(Cp)

    # Provide player and computers stats
    P1.stat_output()
    Cp.stat_output()

    choices = {1: "Strike", 2: "Parry", 3: "Block", 4: "Heal"}

    print(
        f"\nWhat will you do {P1.name}?\n\n   [1] Strike\n   [2] Parry\n   [3] Block\n   [4] Heal\n"
    )

    # Get player decision for this turn
    p1_choice = int(input("Decision: "))
    print(f"\n{P1.name} decides to {choices[p1_choice]}\n")

    # Get computer decision for this turn and print choice
    cp_choice = 1
    print(f"{Cp.name} decides to {choices[cp_choice]}\n")

    # Decide round outcome
    outcome(P1, Cp, p1_choice, cp_choice)

    # Check if the player has died
    if P1.health <= 0:
        print("You are dead.")
        run = False
    elif Cp.health <= 0:
        print("Victory!")
        run = False
