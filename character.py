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
        self.slime -= 3
        return self.damage

    def parry(self):
        self.slime -= 4
        return self.damage * 1.5

    def block(self):
        self.slime -= 2
        return 30

    def Heal(self):
        self.slime -= 3
        self.health += 30
        return self.health

    def stat_output(self):
        # Returns the attributes from the character objects
        print(f"\n{self.name}\n   HP: {self.health} | SLIME: {self.slime}")


if __name__ == "__main__":
    pass
