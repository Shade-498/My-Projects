class Character:
    max_level = 3
    def __init__(self, *, level: int) -> None:
        # Initialize character stats based on level
        self.level = level
        self.health_points = self.base_health_points * level
        self.attack_power = self.base_attack_power * level

    def attack(self, *, target: "Character") -> None:
        # Perform attack on target
        target.got_damage(damage=self.attack_power)

    def got_damage(self, *, damage: int) -> None:        # Calculate and apply damage considering defense
        damage = damage * (100 - self.defence) / 100
        damage = round(damage)
        self.health_points -= damage

    def is_alive(self) -> bool:
        # Check if character has health points remaining
        return self.health_points > 0

    @property
    def defence(self) -> int:
        # Calculate defense based on level
        defence = self.base_defence * self.level
        return defence

    @property
    def max_health_points(self) -> int:
        # Calculate maximum possible health points
        return self.level * self.base_health_points

    def health_points_percent(self):
        # Calculate remaining health as percentage
        return 100 * self.health_points / self.max_health_points

    def level_up(self):
        # Increase level and heal if below max level
        if self.level < self.max_level:
            self.level += 1
            self.health_points += int(self.max_health_points / 2)

    def __str__(self) -> str:
        return f"{self.character_name} (level: {self.level}, hp: {self.health_points})"


class Ork(Character):
    base_health_points = 100
    base_attack_power = 10
    character_name = "Ork"
    base_defence = 15

    @property
    def defence(self) -> int:
        # Triple defense when below 50 HP
        defence = super().defence
        if self.health_points < 50:
            defence *= 3

        return defence


class Elf(Character):
    base_health_points = 50
    base_attack_power = 15
    character_name = "Elf"
    base_defence = 10

    def attack(self, *, target: "Character") -> None:
        # Triple damage against targets below 30% health
        attack_power = self.attack_power
        if target.health_points_percent() < 30:
            attack_power = self.attack_power * 3
        target.got_damage(damage=attack_power)


ork = Ork(level=1)
elf = Elf(level=1)


def fight(*, character_1: Character, character_2: Character) -> None:
    # Combat loop until one character dies
    print("Fight started", character_1, character_2)
    while character_1.is_alive() and character_2.is_alive():
        character_1.attack(target=character_2)
        print(character_2)
        if character_2.is_alive():
            character_2.attack(target=character_1)
            print(character_1)

    # Level up winner and display results
    if character_1.is_alive():
        character_1.level_up()
    else:
        character_2.level_up()

    print(f"{character_1.character_name} is {'alive' if character_1.is_alive() else 'dead'}", character_1)
    print(f"{character_2.character_name} is {'alive' if character_2.is_alive() else 'dead'}", character_2)


fight(character_1=ork, character_2=elf)