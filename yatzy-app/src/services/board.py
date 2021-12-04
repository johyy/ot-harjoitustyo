class Board:

    def check_aces(self, dice_list):
        if 1 in dice_list:
            return True

    def check_twos(self, dice_list):
        if 2 in dice_list:
            return True

    def check_threes(self, dice_list):
        if 3 in dice_list:
            return True

    def check_fours(self, dice_list):
        if 4 in dice_list:
            return True

    def check_fives(self, dice_list):
        if 5 in dice_list:
            return True

    def check_sixes(self, dice_list):
        if 6 in dice_list:
            return True

    def check_pair(self, dice_list):
        dice_list.sort()
        if len(dice_list) == 2:
            if dice_list[0] == dice_list[1]:
                return True
        if len(dice_list) == 3:
            if dice_list[0] == dice_list[1] or dice_list[1] == dice_list[2]:
                return True
        if len(dice_list) == 4:
            if dice_list[0] == dice_list[1] or dice_list[1] == dice_list[2]:
                return True
            if dice_list[2] == dice_list[3]:
                return True
        if len(dice_list) == 5:
            if dice_list[0] == dice_list[1] or dice_list[1] == dice_list[2]:
                return True
            if dice_list[2] == dice_list[3] or dice_list[3] == dice_list[4]:
                return True

    def check_two_pairs(self, dice_list):
        dice_list.sort()
        if len(dice_list) == 4:
            if dice_list[0] == dice_list[1] and dice_list[2] == dice_list[3]:
                return True
        if len(dice_list) == 5:
            if dice_list[0] == dice_list[1] and dice_list[2] == dice_list[3]:
                return True
            if dice_list[1] == dice_list[2] and dice_list[3] == dice_list[4]:
                return True

    def check_three_kind(self, dice_list):
        dice_list.sort()
        if len(dice_list) == 3:
            if dice_list[0] == dice_list[1] and dice_list[1] == dice_list[2]:
                return True
        if len(dice_list) > 3:
            if dice_list[0] == dice_list[1] and dice_list[1] == dice_list[2]:
                return True
            if dice_list[1] == dice_list[2] and dice_list[2] == dice_list[3]:
                return True
        if len(dice_list) > 4:
            if dice_list[0] == dice_list[1] and dice_list[1] == dice_list[2]:
                return True
            if dice_list[1] == dice_list[2] and dice_list[2] == dice_list[3]:
                return True
            if dice_list[2] == dice_list[3] and dice_list[3] == dice_list[4]:
                return True

    def check_four_kind(self, dice_list):
        dice_list.sort()
        if len(dice_list) >= 4:
            if dice_list[0] == dice_list[1] and dice_list[1] == dice_list[2] and dice_list[2] == dice_list[3]:
                return True
            if dice_list[1] == dice_list[2] and dice_list[2] == dice_list[3] and dice_list[3] == dice_list[4]:
                return True

    def check_full_house(self, dice_list):
        dice_list.sort()
        if len(dice_list) == 5:
            if dice_list[0] == dice_list[1] and dice_list[1] == dice_list[2]:
                if dice_list[3] == dice_list[4]:
                    return True
            if dice_list[0] == dice_list[1]:
                if dice_list[2] == dice_list[3] and dice_list[3] == dice_list[4]:
                    return True

    def check_small_straight(self, dice_list):
        if len(dice_list) == 5:
            dice_list.sort()
            if dice_list[0] == 1 and dice_list[1] == 2 and dice_list[2] == 3 and dice_list[3] == 4 and dice_list[4] == 5:
                return True

    def check_large_straight(self, dice_list):
        if len(dice_list) == 5:
            dice_list.sort()
            if dice_list[0] == 2 and dice_list[1] == 3 and dice_list[2] == 4 and dice_list[3] == 5 and dice_list[4] == 6:
                return True

    def check_yatzy(self, dice_list):
        dice_list.sort()
        if len(dice_list) == 5:
            if dice_list[0] == dice_list[4]:
                return True
    
    def aces(self, dice_list):
        new_list = []
        new_sum = 0
        for die in dice_list:
            if die == 1:
                new_list.append(die)
        for die in new_list:
            new_sum += die
        return new_sum