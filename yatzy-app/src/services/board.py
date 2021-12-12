class Board:

    table = {"Aces": '-', "Twos": '-', "Threes": '-', "Fours": '-', "Fives": '-', "Sixes": '-', "Bonus": '0', "Three of a kind": '-',
             "Four of a kind": '-', "Full house": '-', "Small straight": '-', "Large straight": '-', "Chance": '-', "Yatzy": '-'}

    def check_aces(self, dice_list):
        if 1 in dice_list:
            return True
        return False

    def check_twos(self, dice_list):
        if 2 in dice_list:
            return True
        return False

    def check_threes(self, dice_list):
        if 3 in dice_list:
            return True
        return False

    def check_fours(self, dice_list):
        if 4 in dice_list:
            return True
        return False

    def check_fives(self, dice_list):
        if 5 in dice_list:
            return True
        return False

    def check_sixes(self, dice_list):
        if 6 in dice_list:
            return True
        return False

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
        return False

    def check_four_kind(self, dice_list):
        dice_list.sort()
        if len(dice_list) == 4:
            if dice_list[0] == dice_list[1] and dice_list[1] == dice_list[2] and dice_list[2] == dice_list[3]:
                return True
        if len(dice_list) == 5:
            if dice_list[0] == dice_list[1] and dice_list[1] == dice_list[2] and dice_list[2] == dice_list[3]:
                return True
            if dice_list[1] == dice_list[2] and dice_list[2] == dice_list[3] and dice_list[3] == dice_list[4]:
                return True
        return False

    def check_full_house(self, dice_list):
        dice_list.sort()
        if len(dice_list) == 5:
            if dice_list[0] == dice_list[1] and dice_list[1] == dice_list[2]:
                if dice_list[3] == dice_list[4]:
                    return True
            if dice_list[0] == dice_list[1]:
                if dice_list[2] == dice_list[3] and dice_list[3] == dice_list[4]:
                    return True
        return False

    def check_small_straight(self, dice_list):
        if len(dice_list) == 5:
            dice_list.sort()
            if dice_list[0] == 1 and dice_list[1] == 2 and dice_list[2] == 3 and dice_list[3] == 4 and dice_list[4] == 5:
                return True
        return False

    def check_large_straight(self, dice_list):
        if len(dice_list) == 5:
            dice_list.sort()
            if dice_list[0] == 2 and dice_list[1] == 3 and dice_list[2] == 4 and dice_list[3] == 5 and dice_list[4] == 6:
                return True
        return False

    def check_yatzy(self, dice_list):
        dice_list.sort()
        if len(dice_list) == 5:
            if dice_list[0] == dice_list[4]:
                return True
        return False

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
        if len(dice_list) == 4:
            if dice_list[0] == dice_list[1] and dice_list[1] == dice_list[2]:
                new_list.append(dice_list[0])
                new_list.append(dice_list[1])
                new_list.append(dice_list[2])
            elif dice_list[1] == dice_list[2] and dice_list[2] == dice_list[3]:
                new_list.append(dice_list[1])
                new_list.append(dice_list[2])
                new_list.append(dice_list[3])
        if len(dice_list) == 5:
            if dice_list[0] == dice_list[1] and dice_list[1] == dice_list[2]:
                new_list.append(dice_list[0])
                new_list.append(dice_list[1])
                new_list.append(dice_list[2])
            elif dice_list[1] == dice_list[2] and dice_list[2] == dice_list[3]:
                new_list.append(dice_list[1])
                new_list.append(dice_list[2])
                new_list.append(dice_list[3])
            elif dice_list[2] == dice_list[3] and dice_list[3] == dice_list[4]:
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
            elif dice_list[3] == dice_list[4]:
                new_list.append(dice_list[1])
                new_list.append(dice_list[2])
                new_list.append(dice_list[3])
                new_list.append(dice_list[4])
        for die in new_list:
            new_sum += die
        return new_sum

    def mark_aces(self, dice):
        if self.table["Aces"] == "-":
            self.table["Aces"] = self.aces(dice)
            self.check_if_bonus()
            return True
        return False

    def mark_twos(self, dice):
        if self.table["Twos"] == "-":
            self.table["Twos"] = self.twos(dice)
            self.check_if_bonus()
            return True
        return False

    def mark_threes(self, dice):
        if self.table["Threes"] == "-":
            self.table["Threes"] = self.threes(dice)
            self.check_if_bonus()
            return True
        return False

    def mark_fours(self, dice):
        if self.table["Fours"] == "-":
            self.table["Fours"] = self.fours(dice)
            self.check_if_bonus()
            return True
        return False

    def mark_fives(self, dice):
        if self.table["Fives"] == "-":
            self.table["Fives"] = self.fives(dice)
            self.check_if_bonus()
            return True
        return False

    def mark_sixes(self, dice):
        if self.table["Sixes"] == "-":
            self.table["Sixes"] = self.sixes(dice)
            self.check_if_bonus()
            return True
        return False

    def mark_three_same(self, dice):
        if self.table["Three of a kind"] == "-":
            self.table["Three of a kind"] = self.three_same(dice)
            return True
        return False

    def mark_four_same(self, dice):
        if self.table["Four of a kind"] == "-":
            self.table["Four of a kind"] = self.four_same(dice)
            return True
        return False

    def mark_full_house(self, new_sum):
        if self.table["Full house"] == "-":
            self.table["Full house"] = new_sum
            return True
        return False

    def mark_small_straight(self, num):
        if self.table["Small straight"] == "-":
            self.table["Small straight"] = num
            return True
        return False

    def mark_large_straight(self, num):
        if self.table["Large straight"] == "-":
            self.table["Large straight"] = num
            return True
        return False

    def mark_chance(self, new_sum):
        if self.table["Chance"] == "-":
            self.table["Chance"] = new_sum
            return True
        return False

    def mark_yatzy(self, num):
        if self.table["Yatzy"] == "-":
            self.table["Yatzy"] = num
            return True
        return False

    def get_table(self):
        return self.table

    def check_if_full(self):
        for number in self.table:
            if self.table[number] == "-":
                return False
        return True

    def check_if_bonus(self):
        bonus_sum = 0
        if self.table["Aces"] != "-" and self.table["Twos"] != "-" and self.table["Threes"] != "-" and self.table["Fours"] != "-" and self.table["Fives"] != "-" and self.table["Sixes"] != "-":
            bonus_sum += self.table["Aces"]
            bonus_sum += self.table["Twos"]
            bonus_sum += self.table["Threes"]
            bonus_sum += self.table["Fours"]
            bonus_sum += self.table["Fives"]
            bonus_sum += self.table["Sixes"]
        if bonus_sum >= 63:
            self.table["Bonus"] = 50

    def count_total(self):
        total_sum = 0
        for number in self.table:
            total_sum += int(self.table[number])
        return str(total_sum)
