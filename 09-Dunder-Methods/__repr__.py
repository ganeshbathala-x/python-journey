class Gamer:
    def __init__(self,username,game,rank):
        self.username=username
        self.game=game
        self.rank=rank
    def __str__(self):
        return f"username:,{self.username},game:{self.game},rank:{self.rank}"
    def __repr__(self):
        return f"Gamer(username={self.username!r},game={self.game!r},rank={self.rank!r})"
gamer=Gamer("leo","Free Fire","diamond")
print(gamer)
print(repr(gamer))