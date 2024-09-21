class Superhero:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def info(self):
        return (f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Super Power: {self.super_power}\n"
                f"Weapon: {self.weapon}\n")

    def is_leader(self):
        return self.name == "Captain America"


# list of data
super_heroes = [
    Superhero("Captain America", 102, "Male", "Super Strength", "Shield"),
    Superhero("Iron Man", 48, "Male", "Technology", "Armor"),
    Superhero("Black Widow", 36, "Female", "Superhuman", "Batons"),
    Superhero("Hulk", 45, "Male", "Unlimited Strength", "No Weapon"),
    Superhero("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Superhero("Hawkeye", 40, "Male", "Fighting Skills", "Bow and Arrows")
]

# Display information
for hero in super_heroes:
    print(hero.info())
    print(f"Is Leader: {'Yes' if hero.is_leader() else 'No'}")
    print("-" * 30)
