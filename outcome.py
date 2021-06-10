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
