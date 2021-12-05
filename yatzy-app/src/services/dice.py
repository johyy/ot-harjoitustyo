from random import randint


class Dice:

    def roll_dice(self, dice):
        new_dice = []
        for die in dice:
            die = randint(1, 6)
            new_dice.append(die)
        return new_dice

    def mix_dice(self, dice, selected_dice):
        mixed_dice = []
        for die1 in dice:
            mixed_dice.append(die1)
        if len(selected_dice) > 0:
            for die2 in selected_dice:
                mixed_dice.append(die2)
        return mixed_dice

    def dice_total(self, dice):
        new_sum = 0
        i = 0
        while i < len(dice):
            new_sum += dice[i]
            i += 1
        return new_sum
