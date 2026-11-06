class GameInventory:
    def __init__(self):
        self.games=[]
    def add_game(self,game):
        self.games.append(game)
    def remove_game(self,game):
        self.games.remove(game)
    def __len__(self):
        return len(self.games)

inventory=GameInventory()
inventory.add_game("Free Fire")
inventory.add_game("Bgmi")
inventory.add_game("Gta")

print(len(inventory))
inventory.remove_game("Bgmi")
print(len(inventory))