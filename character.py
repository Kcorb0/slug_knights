class Character:
    def __init__(self, name, damage=30, slime=10, health=100):
        self.name = name
        self.damage = damage
        self.slime = slime
        self.health = health

        self.slime_warning = f"{self.name} you outa slime bruh."

    def __repr__(self):
        return f"Character({self.name}, {self.damage}, {self.slime}, {self.health})"

    def take_damage(self, dmg):
        self.health -= dmg

    def strike(self):
        cost = 3
        if self.slime < cost:
            print(self.slime_warning)
            return 0
        else:
            self.slime -= cost
            return self.damage

    def parry(self):
        cost = 5
        if self.slime < cost:
            print(self.slime_warning)
            return 0
        else:
            self.slime -= cost
            return self.damage * 1.5

    def block(self):
        cost = 2
        if self.slime < cost:
            print(self.slime_warning)
            return 0
        else:
            self.slime -= cost
            return 30

    def heal(self):
        cost = 6
        if self.slime < cost:
            print(self.slime_warning)
            return 0
        else:
            self.slime -= cost
            self.health += 25

    def stat_output(self):
        # Returns the attributes from the character objects
        print(f"\n{self.name}\n   HP: {self.health} | SLIME: {self.slime}")

    def check_slime(self, increment):
        # Increments slime by 1 each round, slime does not exceed 1
        if self.slime <= 10:
            self.slime += increment
            if self.slime > 10:
                self.slime = 10

    def check_health(self, max_health):
        if self.health > max_health:
            self.health = max_health


if __name__ == "__main__":
    pass
