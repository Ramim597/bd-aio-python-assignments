# Q8: Create a class Player with:
# - a class variable player_count
# - instance variables name and level

# Track how many players were created.


class Player:
    player_count = 0

    def __init__(self, name, level):  # level means (RANK)
        self.name = name
        self.level = level
        Player.player_count += 1


p1 = Player("Ramim", 5)
p1 = Player("Jahid", 10)
print(p1.name, p1.level, Player.player_count)
