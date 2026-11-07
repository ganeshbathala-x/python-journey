class Game:
    def __init__(self,name,rating,players_count):
        self.name=name
        self.rating=rating
        self.players_count=players_count
    def __lt__(self,other):
        return self.rating<other.rating

g1 =Game("bgmi",8.5,100)
g2=Game("gta",9.2,800)
g3=Game("free fire",7.8,200)
print(g1<g2)
games=[g1,g2,g3]
games.sort()
for game in games:
    print(game.name,game.rating)