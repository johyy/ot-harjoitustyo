class Player:
    """Luokka, joka kuvaa yksittäistä pelaajaa.
    Attributes:
        playername: Merkkijonoarvo, joka kuvaa pelaajan pelaajanimeä.
    """

    def __init__(self, playername):
        """Luokan konstruktori, joka luo uuden pelaaja.

        Args:
            playername: Merkkijonoarvo, joka kuvaa pelaajan pelaajanimeä.
        """
        
        self.playername = playername
