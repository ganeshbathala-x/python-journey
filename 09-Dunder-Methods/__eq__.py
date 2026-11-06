class Player:
    def __init__(self,player_id,username,game):
        self.player_id=player_id
        self.username=username
        self.game=game
    def __eq__(self,other):
        if isinstance(other,Player):
            return self.player_id==other.player_id
        return False
p1=Player(101,"monster","bgmi")
p2=Player(101,"leo","gta")
p3=Player(102,"monster","bgmi")

print(p1==p2)
print(p1==p3)
print(p1==100)