class Player:

    def __init__(self):
        self.names =[]
    
    def add_player_to_list(self, playername: str):
        self.names.append(playername)
        for name in self.names:
            print(name)