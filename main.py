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
            player.take_damage(computer.strike())
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

    clear_round()  # Clear Console after round

    max_health = 150  # Max reachable health
    slime_inc = 1  # Slime gain at start of round

    # Print round number and increase round num by 1
    # Check health and slime
    # Provide player and computers stats
    print(f"\n====== Round {round_num} ======")

    P1.check_health(max_health)
    Cp.check_health(max_health)
    P1.check_slime(slime_inc)
    Cp.check_slime(slime_inc)
    P1.stat_output()
    Cp.stat_output()

    choices = {1: "Strike", 2: "Parry", 3: "Block", 4: "Heal"}
    player_options = f"\nWhat will you do {P1.name}?\n   [1] Strike 3s\n   [2] Parry 4s\n   [3] Block 2s\n   [4] Heal 4s\n"
    print(player_options)

    # Get player decision for this turn
    while True:
        p1_choice = input("Decision: ")

        if p1_choice in [str(i) for i in range(1, 5)]:
            break
        else:
            print("Please enter a number between 1 and 4.")

    print(f"\n{P1.name} decides to {choices[int(p1_choice)]}\n")

    # Get computer decision for this turn and print choice
    cp_choice = rand.randint(1, 4)
    print(f"{Cp.name} decides to {choices[cp_choice]}\n")

    # Decide round outcome
    outcome(P1, Cp, int(p1_choice), cp_choice)

    # Check if the player has died
    if P1.health <= 0:
        print("You are dead.\n")
        run = False
        break
    elif Cp.health <= 0:
        print("Victory!\n")
        run = False
        break

    resume = input("Press [Enter] for next round or [x] to exit")
    if resume == "x":
        run = False

    round_num += 1
