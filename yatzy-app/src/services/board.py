class Board:

    table = {"Aces": '-', "Twos": '-', "Threes": '-', "Fours": '-', "Fives": '-', "Sixes": '-', "Bonus": '-', "Three of a kind": '-',
             "Four of a kind": '-', "Full house": '-', "Small straight": '-', "Large straight": '-', "Chance": '-', "Yatzy": '-'}

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

    def twos(self, dice_list):
        new_list = []
        new_sum = 0
        for die in dice_list:
            if die == 2:
                new_list.append(die)
        for die in new_list:
            new_sum += die
        return new_sum

    def threes(self, dice_list):
        new_list = []
        new_sum = 0
        for die in dice_list:
            if die == 3:
                new_list.append(die)
        for die in new_list:
            new_sum += die
        return new_sum

    def fours(self, dice_list):
        new_list = []
        new_sum = 0
        for die in dice_list:
            if die == 4:
                new_list.append(die)
        for die in new_list:
            new_sum += die
        return new_sum

    def fives(self, dice_list):
        new_list = []
        new_sum = 0
        for die in dice_list:
            if die == 5:
                new_list.append(die)
        for die in new_list:
            new_sum += die
        return new_sum

    def sixes(self, dice_list):
        new_list = []
        new_sum = 0
        for die in dice_list:
            if die == 6:
                new_list.append(die)
        for die in new_list:
            new_sum += die
        return new_sum

    def three_same(self, dice_list):
        new_list = []
        new_sum = 0
        dice_list.sort()
        if len(dice_list) == 3:
            for die in dice_list:
                new_list.append(die)
        if len(dice_list) > 3:
            if dice_list[0] == dice_list[1] and dice_list[1] == dice_list[2]:
                new_list.append(dice_list[0])
                new_list.append(dice_list[1])
                new_list.append(dice_list[2])
            if dice_list[1] == dice_list[2] and dice_list[2] == dice_list[3]:
                new_list.append(dice_list[1])
                new_list.append(dice_list[2])
                new_list.append(dice_list[3])
        if len(dice_list) > 4:
            if dice_list[0] == dice_list[1] and dice_list[1] == dice_list[2]:
                new_list.append(dice_list[0])
                new_list.append(dice_list[1])
                new_list.append(dice_list[2])
            if dice_list[1] == dice_list[2] and dice_list[2] == dice_list[3]:
                new_list.append(dice_list[1])
                new_list.append(dice_list[2])
                new_list.append(dice_list[3])
            if dice_list[2] == dice_list[3] and dice_list[3] == dice_list[4]:
                new_list.append(dice_list[2])
                new_list.append(dice_list[3])
                new_list.append(dice_list[4])
        for die in new_list:
            new_sum += die
        return new_sum

    def four_same(self, dice_list):
        new_list = []
        new_sum = 0
        dice_list.sort()
        if len(dice_list) == 4:
            for die in dice_list:
                new_list.append(die)
        if len(dice_list) > 4:
            if dice_list[0] == dice_list[1]:
                new_list.append(dice_list[0])
                new_list.append(dice_list[1])
                new_list.append(dice_list[2])
                new_list.append(dice_list[3])
            if dice_list[3] == dice_list[4]:
                new_list.append(dice_list[1])
                new_list.append(dice_list[2])
                new_list.append(dice_list[3])
                new_list.append(dice_list[4])
        for die in new_list:
            new_sum += die
        return new_sum

    def mark_aces(self, dice):
        self.table["Aces"] = self.aces(dice)

    def mark_twos(self, dice):
        self.table["Twos"] = self.twos(dice)

    def mark_threes(self, dice):
        self.table["Threes"] = self.threes(dice)

    def mark_fours(self, dice):
        self.table["Fours"] = self.fours(dice)

    def mark_fives(self, dice):
        self.table["Fives"] = self.fives(dice)

    def mark_sixes(self, dice):
        self.table["Sixes"] = self.sixes(dice)

    def mark_three_same(self, dice):
        self.table["Three of a kind"] = self.three_same(dice)

    def mark_four_same(self, dice):
        self.table["Four of a kind"] = self.four_same(dice)

    def mark_full_house(self, new_sum):
        self.table["Full house"] = new_sum

    def mark_small_straight(self):
        self.table["Small straight"] = 15

    def mark_large_straight(self):
        self.table["Large straight"] = 20

    def mark_chance(self, new_sum):
        self.table["Chance"] = new_sum

    def mark_yatzy(self, new_sum):
        self.table["Yatzy"] = new_sum

    def get_table(self):
        return self.table
