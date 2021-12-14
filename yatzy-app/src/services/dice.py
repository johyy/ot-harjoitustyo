from random import randint


class Dice:
    """Noppien sovelluslogiikasta vastaava luokka"""

    def roll_dice(self, dice):
        """Arpoo listalle uudet numerot välillä 1-6.
        
        Args:
            dice: Lista nopan silmälukuja kuvaavista luvuista.
        Returns:
            Lista, jossa on uudet, arvotut luvut.    
        """

        rolled_dice = []
        for die in dice:
            die = randint(1, 6)
            rolled_dice.append(die)
        return rolled_dice

    def mix_dice(self, dice, selected_dice):
        """Sekoittaa listan tallennetuista luvuista listaan uudelleen arvotuista luvuista.
        
        Args:
            dice: Lista nopan silmälukuja kuvaavista luvuista, jotka on arvottu uudelleen käyttäen metodia roll_dice().
            selected_dice: Lista nopan silmälukuja kuvaavista luvuista, jotka on aiemmin valittu tallennettaviksi.
        Returns:
            Lista, jossa on yhteensä viisi nopan silmälukua kuvaavaa lukua, jotka on saatu listoista "dice" ja "selected_dice".
        """

        mixed_dice = []
        for die1 in dice:
            mixed_dice.append(die1)
        if len(selected_dice) > 0:
            for die2 in selected_dice:
                mixed_dice.append(die2)
        return mixed_dice

    def dice_total(self, dice):
        """Laskee yhteen listan luvut.
        
        Args:
            dice: Lista nopan silmälukuja kuvaavista luvuista, jotka halutaan laskea yhteen.
        Returns:
            Summa yhteenlasketuista luvuista.        
        """
        
        new_sum = 0
        i = 0
        while i < len(dice):
            new_sum += dice[i]
            i += 1
        return new_sum
