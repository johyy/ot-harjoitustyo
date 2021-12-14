class Board:
    """Pelilaudan sovelluslogiikasta vastaava luokka."""

    table = {"Aces": '-', "Twos": '-', "Threes": '-', "Fours": '-', "Fives": '-', "Sixes": '-', "Bonus": '0', "Three of a kind": '-',
             "Four of a kind": '-', "Full house": '-', "Small straight": '-', "Large straight": '-', "Chance": '-', "Yatzy": '-'}

    def check_numbers(self, dice_list, number):
        """Käy läpi listan etsien haluttua lukua.

        Args:
            dice_list: Lista, joka kuvaa tarkasteltavana olevien noppien silmälukuja.
            number: Luku, joka kuvaa nopan silmälukua, jota halutaan etsiä.
        Returns:
            True/False riippuen siitä, löytyykö haluttua silmälukua.
        """

        if number in dice_list:
            return True
        return False

    def check_three_kind(self, dice_list):
        """Käy läpi listan etsien kolmea samaa lukua.

        Args:
            dice_list: Lista, joka kuvaa tarkasteltavana olevien noppien silmälukuja.
        Returns:
            True/False riippuen siitä, löytyykö kolmea samaa silmälukua.
        """

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
        """Käy läpi listan etsien neljää samaa lukua.

        Args:
            dice_list: Lista, joka kuvaa tarkasteltavana olevien noppien silmälukuja.
        Returns:
            True/False riippuen siitä, löytyykö neljää samaa silmälukua.
        """

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
        """Käy läpi listan etsien sekä kolmea samaa lukua, että kahta samaa lukua.

        Args:
            dice_list: Lista, joka kuvaa tarkasteltavana olevien noppien silmälukuja.
        Returns:
            True/False riippuen siitä, löytyykö haluttu määrä samoja (3+2) silmälukuja.
        """

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
        """Käy läpi listan etsien lukuja 1, 2, 3, 4 ja 5.

        Args:
            dice_list: Lista, joka kuvaa tarkasteltavana olevien noppien silmälukuja.
        Returns:
            True/False riippuen siitä, löytyykö haluttuja silmälukuja.
        """

        if len(dice_list) == 5:
            dice_list.sort()
            if dice_list[0] == 1 and dice_list[1] == 2 and dice_list[2] == 3 and dice_list[3] == 4 and dice_list[4] == 5:
                return True
        return False

    def check_large_straight(self, dice_list):
        """Käy läpi listan etsien lukuja 2, 3, 2, 5 ja 6.

        Args:
            dice_list: Lista, joka kuvaa tarkasteltavana olevien noppien silmälukuja.
        Returns:
            True/False riippuen siitä, löytyykö haluttuja silmälukuja.
        """

        if len(dice_list) == 5:
            dice_list.sort()
            if dice_list[0] == 2 and dice_list[1] == 3 and dice_list[2] == 4 and dice_list[3] == 5 and dice_list[4] == 6:
                return True
        return False

    def check_yatzy(self, dice_list):
        """Käy läpi listan ja tarkistaa, että kaikki luvut omat samoja ja että niitä on viisi.

        Args:
            dice_list: Lista, joka kuvaa tarkasteltavana olevien noppien silmälukuja.
        Returns:
            True/False riippuen siitä, löytyykö viisi samaa silmälukua.
        """

        dice_list.sort()
        if len(dice_list) == 5:
            if dice_list[0] == dice_list[4]:
                return True
        return False

    def numbers(self, dice_list, number):
        """Laskee listalta halutun numeron esiintymät yhteet.

        Args:
            dice_list: Lista, joka kuvaa tarkasteltavana olevien noppien silmälukuja.
            number: Haluttu silmäluku, jonka kaikki esiintymät lasketaan yhteen.
        Returns:
            Summa, johon on laskettu haluttu summa niin monta kertaa, kuin se esiintyy listassa.
        """

        new_list = []
        new_sum = 0
        for die in dice_list:
            if die == number:
                new_list.append(die)
        for die in new_list:
            new_sum += die
        return new_sum

    def three_same(self, dice_list):
        """Laskee listalta kolme kertaa esiintyvän silmäluvun luvut yhteet.

        Args:
            dice_list: Lista, joka kuvaa tarkasteltavana olevien noppien silmälukuja.
        Returns:
            Summa, johon on laskettu kolme kertaa esiintyvän silmäluvun yhteenlaskusta.
        """

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
        """Laskee listalta neljä kertaa esiintyvän silmäluvun luvut yhteet.

        Args:
            dice_list: Lista, joka kuvaa tarkasteltavana olevien noppien silmälukuja.
        Returns:
            Summa, johon on laskettu neljä kertaa esiintyvän silmäluvun yhteenlaskusta.
        """

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
        """Lisää pelilaudalle saadun tuloksen, mikäli se on tyhjä. Tarkistaa myös onko kyseessä viimeinen numero, jonka jälkeen merkataan mahdollisesti bonus.

        Args:
            dice: Kuvaa noppien silmälukuja, joista tarkistetaan oikea käytettävä summa metodilla self.numbers().
        Returns:
            True/False riippuen siitä, saadaanko tulosta merkattua vai ei.
        """

        if self.table["Aces"] == "-":
            self.table["Aces"] = self.numbers(dice, 1)
            self.check_if_bonus()
            return True
        return False

    def mark_twos(self, dice):
        """Lisää pelilaudalle saadun tuloksen, mikäli se on tyhjä. Tarkistaa myös onko kyseessä viimeinen numero, jonka jälkeen merkataan mahdollisesti bonus.

        Args:
            dice: Kuvaa noppien silmälukuja, joista tarkistetaan oikea käytettävä summa metodilla self.numbers().
        Returns:
            True/False riippuen siitä, saadaanko tulosta merkattua vai ei.
        """

        if self.table["Twos"] == "-":
            self.table["Twos"] = self.numbers(dice, 2)
            self.check_if_bonus()
            return True
        return False

    def mark_threes(self, dice):
        """Lisää pelilaudalle saadun tuloksen, mikäli se on tyhjä. Tarkistaa myös onko kyseessä viimeinen numero, jonka jälkeen merkataan mahdollisesti bonus.

        Args:
            dice: Kuvaa noppien silmälukuja, joista tarkistetaan oikea käytettävä summa metodilla self.numbers().
        Returns:
            True/False riippuen siitä, saadaanko tulosta merkattua vai ei.
        """

        if self.table["Threes"] == "-":
            self.table["Threes"] = self.numbers(dice, 3)
            self.check_if_bonus()
            return True
        return False

    def mark_fours(self, dice):
        """Lisää pelilaudalle saadun tuloksen, mikäli se on tyhjä. Tarkistaa myös onko kyseessä viimeinen numero, jonka jälkeen merkataan mahdollisesti bonus.

        Args:
            dice: Kuvaa noppien silmälukuja, joista tarkistetaan oikea käytettävä summa metodilla self.numbers().
        Returns:
            True/False riippuen siitä, saadaanko tulosta merkattua vai ei.
        """

        if self.table["Fours"] == "-":
            self.table["Fours"] = self.numbers(dice, 4)
            self.check_if_bonus()
            return True
        return False

    def mark_fives(self, dice):
        """Lisää pelilaudalle saadun tuloksen, mikäli se on tyhjä. Tarkistaa myös onko kyseessä viimeinen numero, jonka jälkeen merkataan mahdollisesti bonus.

        Args:
            dice: Kuvaa noppien silmälukuja, joista tarkistetaan oikea käytettävä summa metodilla self.numbers().
        Returns:
            True/False riippuen siitä, saadaanko tulosta merkattua vai ei.
        """

        if self.table["Fives"] == "-":
            self.table["Fives"] = self.numbers(dice, 5)
            self.check_if_bonus()
            return True
        return False

    def mark_sixes(self, dice):
        """Lisää pelilaudalle saadun tuloksen, mikäli se on tyhjä. Tarkistaa myös onko kyseessä viimeinen numero, jonka jälkeen merkataan mahdollisesti bonus.

        Args:
            dice: Kuvaa noppien silmälukuja, joista tarkistetaan oikea käytettävä summa metodilla self.numbers().
        Returns:
            True/False riippuen siitä, saadaanko tulosta merkattua vai ei.
        """

        if self.table["Sixes"] == "-":
            self.table["Sixes"] = self.numbers(dice, 6)
            self.check_if_bonus()
            return True
        return False

    def mark_three_same(self, dice):
        """Lisää pelilaudalle saadun tuloksen, mikäli se on tyhjä.

        Args:
            dice: Kuvaa noppien silmälukuja, joista tarkistetaan oikea käytettävä summa metodilla self.three_same().
        Returns:
            True/False riippuen siitä, saadaanko tulosta merkattua vai ei.
        """

        if self.table["Three of a kind"] == "-":
            self.table["Three of a kind"] = self.three_same(dice)
            return True
        return False

    def mark_four_same(self, dice):
        """Lisää pelilaudalle saadun tuloksen, mikäli se on tyhjä.

        Args:
            dice: Kuvaa noppien silmälukuja, joista tarkistetaan oikea käytettävä summa metodilla self.four_same().
        Returns:
            True/False riippuen siitä, saadaanko tulosta merkattua vai ei.
        """

        if self.table["Four of a kind"] == "-":
            self.table["Four of a kind"] = self.four_same(dice)
            return True
        return False

    def mark_full_house(self, new_sum):
        """Lisää pelilaudalle saadun tuloksen, mikäli se on tyhjä.

        Args:
            new_sum: Kuvaa saadun tuloksen summaa.
        Returns:
            True/False riippuen siitä, saadaanko tulosta merkattua vai ei.
        """

        if self.table["Full house"] == "-":
            self.table["Full house"] = new_sum
            return True
        return False

    def mark_small_straight(self, num):
        """Lisää pelilaudalle saadun tuloksen, mikäli se on tyhjä.

        Args:
            num: Kuvaa lisättävää tulosta.
        Returns:
            True/False riippuen siitä, saadaanko tulosta merkattua vai ei.
        """

        if self.table["Small straight"] == "-":
            self.table["Small straight"] = num
            return True
        return False

    def mark_large_straight(self, num):
        """Lisää pelilaudalle saadun tuloksen, mikäli se on tyhjä.

        Args:
            num: Kuvaa lisättävää tulosta.
        Returns:
            True/False riippuen siitä, saadaanko tulosta merkattua vai ei.
        """

        if self.table["Large straight"] == "-":
            self.table["Large straight"] = num
            return True
        return False

    def mark_chance(self, new_sum):
        """Lisää pelilaudalle saadun tuloksen, mikäli se on tyhjä.

        Args:
            new_sum: Kuvaa saadun tuloksen summaa.
        Returns:
            True/False riippuen siitä, saadaanko tulosta merkattua vai ei.
        """

        if self.table["Chance"] == "-":
            self.table["Chance"] = new_sum
            return True
        return False

    def mark_yatzy(self, num):
        """Lisää pelilaudalle saadun tuloksen, mikäli se on tyhjä.

        Args:
            num: Kuvaa lisättävää tulosta.
        Returns:
            True/False riippuen siitä, saadaanko tulosta merkattua vai ei.
        """

        if self.table["Yatzy"] == "-":
            self.table["Yatzy"] = num
            return True
        return False

    def get_table(self):
        """Palauttaa pelilaudan tulosnäkymän.

        Returns:
            Taulu, jossa näkyy lisätyt ja lisäämättömät tulokset.
        """

        return self.table

    def check_if_full(self):
        """Tarkistaa onko tulostauluun lisätty tulos jokaiseen kohtaan.

        Returns:
            True/False riippuen siitä, onko tulostauluun lisätty tulos jokaiseen kohtaan vai ei.
        """

        for number in self.table:
            if self.table[number] == "-":
                return False
        return True

    def check_if_bonus(self):
        """Tarkistaa onko mahdollista lisätä tulostauluun luku 50 kohdalle "Bonus" ja lisää sen, mikäli mahdollista on. 
            Bonus lisätään kun luvut 1-6 ovat täynnä ja summaltaan yli 63."""

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
        """Laskee yhteen tulostaulun kaikki tulokset kun tauluun on lisätty kaikki tulokset.

        Returns:
            Summa, johon on laskettu yhteen kaikki tulostaulun tulokset.
        """

        total_sum = 0
        for number in self.table:
            total_sum += int(self.table[number])
        return str(total_sum)