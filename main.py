import random as rand
import os
from character import Character

clear_round = lambda: os.system("cls")


def outcome(player, computer, p1_choice, cp_choice):
    # Takes the choices of the player and computer
    # Changes the player and computer objects

    p1 = p1_choice
    cp = cp_choice

    if p1 == 1:
        computer.take_damage(player.strike())
        if cp == 1:
            player.take_damage(computer.strike())
        elif cp == 2:
            computer.health += 20
            player.take_damage(computer.parry())
        elif cp == 3:
            computer.health += (computer.block() * 2) - player.damage
        else:
            computer.heal()

    elif p1 == 2:
        if cp == 1:
            player.health += 20
            computer.take_damage(player.parry())
        elif cp == 2:
            player.parry()
            computer.parry()
        elif cp == 3:
            player.parry()
            computer.block()
        else:
            computer.heal()

    elif p1 == 3:
        if cp == 1:
            player.health += (player.block() * 2) - computer.damage
        elif cp == 2:
            player.block()
            computer.parry()
        elif cp == 3:
            player.block()
            computer.block()
        else:
            computer.heal()

    elif p1 == 4:
        player.heal()
        if cp == 1:
            player.take_damage(computer.strike())
        elif cp == 2:
            computer.parry()
        elif cp == 3:
            computer.block()
        else:
            computer.heal()


title_card = """
        
    ░██████╗██╗░░░░░██╗░░░██╗░██████╗░  ██╗░░██╗███╗░░██╗██╗░██████╗░██╗░░██╗████████╗░██████╗
    ██╔════╝██║░░░░░██║░░░██║██╔════╝░  ██║░██╔╝████╗░██║██║██╔════╝░██║░░██║╚══██╔══╝██╔════╝
    ╚█████╗░██║░░░░░██║░░░██║██║░░██╗░  █████═╝░██╔██╗██║██║██║░░██╗░███████║░░░██║░░░╚█████╗░
    ░╚═══██╗██║░░░░░██║░░░██║██║░░╚██╗  ██╔═██╗░██║╚████║██║██║░░╚██╗██╔══██║░░░██║░░░░╚═══██╗
    ██████╔╝███████╗╚██████╔╝╚██████╔╝  ██║░╚██╗██║░╚███║██║╚██████╔╝██║░░██║░░░██║░░░██████╔╝
    ╚═════╝░╚══════╝░╚═════╝░░╚═════╝░  ╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░
    """

print(title_card)
P1_name = input("What is your slugs name: ").title()
P1 = Character(P1_name)
enemy_slug = ["Slugtron", "King Sludge", "Slick", "Slug on Wheels"][rand.randint(0, 3)]
Cp = Character(enemy_slug)

run = True
round_num = 1

while run:

    # Clear console at the start of round for clarity
    clear_round()

    # Print round number and increase round num by 1
    # Check slime levels
    # Provide player and computers stats
    print(f"\n====== Round {round_num} ======")

    P1.slime_levels(1)
    Cp.slime_levels(1)
    P1.stat_output()
    Cp.stat_output()

    choices = {1: "Strike", 2: "Parry", 3: "Block", 4: "Heal"}
    player_options = f"\nWhat will you do {P1.name}?\n   [1] Strike\n   [2] Parry\n   [3] Block\n   [4] Heal\n"
    print(player_options)

    # Get player decision for this turn
    p1_choice = int(input("Decision: "))
    print(f"\n{P1.name} decides to {choices[p1_choice]}\n")

    # Get computer decision for this turn and print choice
    cp_choice = rand.randint(1, 4)
    print(f"{Cp.name} decides to {choices[cp_choice]}\n")

    # Decide round outcome
    outcome(P1, Cp, p1_choice, cp_choice)

    # Check if the player has died
    if P1.health <= 0:
        print("You are dead.\n")
        run = False
        break
    elif Cp.health <= 0:
        print("Victory!\n")
        run = False
        break

    resume = input("Press [Enter] for next round")

    round_num += 1
