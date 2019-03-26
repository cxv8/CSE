class Item(object):
    def __init__(self, name, material):
        self.name = name
        self.material = material


class Sword(Item):
    def __init__(self, name, material, use=True, equip=True):
        super(Sword, self).__init__(name, material)
        self.equip = equip
        self.use = use

    def hold(self):
        self.equip = True
        print("You have %s equipped." % self.name)

    def swing(self):
        print("You swung your weapon.")

    def stop(self):
        self.use = False
        print("You stopped using the %s" % self.name)

    def unequip(self):
        self.equip = False
        print("You unequipped the item.")


class FireSword(Sword):
    def __init__(self, name, material, shoot=True):
        super(FireSword, self).__init__(name, material)
        self.shoot = shoot
        self.ammo = 5
        self.dmg = 35

    def fireball(self, shots):
        if self.shoot:
            if self.ammo <= 0:
                print("You need to reload.")
            elif self.ammo < shots:
                print("You shot %s fireball and ran out." % self.ammo)
                self.ammo = 0
            else:
                print("You shoot %s fireball(s)." % shots)
                self.ammo -= shots
        else:
            print("You can't shoot.")

    def reload(self):
        self.ammo = 5
        print("Your fire sword is fully charged.")


class LightningSword(Sword):
    def __init__(self, name, material, shoot=True, dmg=45):
        super(LightningSword, self).__init__(name, material)
        self.shoot = shoot
        self.ammo = 5
        self.dmg = dmg

    def lightning(self, shots):
        if self.shoot:
            if self.ammo <= 0:
                print("You need to reload.")
            elif self.ammo < shots:
                print("You shot %s lightning bolt and ran out." % self.ammo)
                self.ammo = 0
            else:
                print("You shoot %s lightning bolt(s)." % shots)
                self.ammo -= shots
        else:
            print("You can't shoot.")

    def reload(self):
        self.ammo = 5
        print("Your lightning sword is fully charged.")


class WindSword(Sword):
    def __init__(self, name, material, shoot=True, dmg=25):
        super(WindSword, self).__init__(name, material)
        self.shoot = shoot
        self.ammo = 5
        self.dmg = dmg

    def wind(self, shots):
        if self.shoot:
            if self.ammo <= 0:
                print("You need to reload.")
            elif self.ammo < shots:
                print("You blew %s gust of wind and ran out." % self.ammo)
                self.ammo = 0
            else:
                print("You blew %s gust of wind(s)." % shots)
                self.ammo -= shots
        else:
            print("You can't shoot.")

    def reload(self):
        self.ammo = 5
        print("Your wind sword is fully charged.")


class WaterSword(Sword):
    def __init__(self, name, material, shoot=True, dmg=25):
        super(WaterSword, self).__init__(name, material)
        self.shoot = shoot
        self.ammo = 5
        self.dmg = dmg

    def water(self, shots):
        if self.shoot:
            if self.ammo <= 0:
                print("You need to reload.")
            elif self.ammo < shots:
                print("You shot %s water bullet and ran out." % self.ammo)
                self.ammo = 0
            else:
                print("You shoot %s water bullet(s)." % shots)
                self.ammo -= shots
        else:
            print("You can't shoot.")

    def reload(self):
        self.ammo = 5
        print("Your water sword is fully charged.")


class EarthSword(Sword):
    def __init__(self, name, material, shoot=True, dmg=30):
        super(EarthSword, self).__init__(name, material)
        self.shoot = shoot
        self.ammo = 5
        self.dmg = dmg

    def earth(self, shots):
        if self.shoot:
            if self.ammo <= 0:
                print("You need to reload.")
            elif self.ammo < shots:
                print("You shot %s block of rock and ran out." % self.ammo)
                self.ammo = 0
            else:
                print("You shoot %s block of rock(s)." % shots)
                self.ammo -= shots
        else:
            print("You can't shoot.")

    def reload(self):
        self.ammo = 5
        print("Your earth sword is fully charged.")


class Bow(Item):
    def __init__(self, name, material):
        super(Bow, self).__init__(name, material)
        self.shoot = True
        self.arrow = 10
        self.dmg = 20

    def shot(self, shots):
        if self.shoot:
            if self.arrow <= 0:
                print("You need to reload.")
            elif self.arrow < shots:
                print("You shot %s arrow and ran out." % self.arrow)
                self.arrow = 0
            else:
                print("You shoot %s arrow(s)." % shots)
                self.arrow -= shots
        else:
            print("You can't shoot.")

    def reload(self):
        self.arrow = 10
        print("You reloaded your arrows.")


class WindBow(Item):
    def __init__(self, name, material, shoot=True):
        super(WindBow, self).__init__(name, material)
        self.shoot = shoot
        self.arrow = 12
        self.dmg = 25

    def shot(self, shots):
        if self.shoot:
            if self.arrow <= 0:
                print("You need to reload.")
            elif self.arrow < shots:
                print("You shot %s wind arrow and ran out." % self.arrow)
            else:
                print("You shoot %s wind arrow(s) knocking your target back." % shots)
                self.arrow -= shots
        else:
            print("You can't shoot.")

    def reload(self):
        self.arrow = 10
        print("You reloaded your arrows.")


class Axe(Sword):
    def __init__(self):
        super(Axe, self).__init__("Starter Axe", "Metal", True, True)
        self.chop_speed = 20


class FasterAxe(Sword):
    def __init__(self):
        super(FasterAxe, self).__init__("Faster Axe", "Speed ore", True, True)
        self.chop_speed = 35


class LongSword(Sword):
    def __init__(self):
        super(LongSword, self).__init__("Long Sword", "Metal", True, True)
        self.dmg = 25


class SLongSword(Sword):
    def __init__(self):
        super(SLongSword, self).__init__("Steel LongSword", "Steel",True, True)
        self.dmg = 35


class HealPotion(Item):
    def __init__(self, name, material, drink=False):
        super(HealPotion, self).__init__(name, material)
        self.drink = drink

    def heal(self):
        if self.drink:
            print("You restored 50 hp.")


class StaminaPotion(Item):
    def __init__(self, name, material, drink=False):
        super(StaminaPotion, self).__init__(name, material)
        self.drink = drink

    def stamina(self):
        if self.drink:
            print("You restored 50 stamina")


class MegaPotion(Item):
    def __init__(self, name, material, drink=False):
        super(MegaPotion, self).__init__(name, material)
        self.drink = drink

    def potion(self):
        if self.potion:
            print("You restored 50 stamina and health")


class SpaceParts(Item):
    def __init__(self, number, combination):
        super(SpaceParts, self).__init__(number, combination)
        self.number = number
        self.combination = combination


class SpacePart1(SpaceParts):
    def __init__(self, number, combination):
        super(SpacePart1, self).__init__('1', '2')
        self.number = number
        self.combination = combination


class SpacePart2(SpaceParts):
    def __init__(self, number, combination):
        super(SpacePart2, self).__init__('2', '3')
        self.number = number
        self.combination = combination


class SpacePart3(SpaceParts):
    def __init__(self, number, combination):
        super(SpacePart3, self).__init__('3', '1')
        self.number = number
        self.combination = combination


class


my_sword = Sword("Starter sword", "Metal")
my_sword.swing()

my_Fsword = FireSword("Fire Sword", "Flame Ore")
my_Fsword.fireball(3)

my_Lsword = LightningSword("Lightning Sword", "Lightning Ore")
my_Lsword.lightning(5)

my_Wsword = WaterSword("Water Sword", "Water Ore")
my_Wsword.water(2)

my_Esword = EarthSword("Earth Sword", "Earth Ore")
my_Esword.swing()

my_WIsword = WindSword("Wind Sword", "Earth Ore")
my_WIsword.wind(3)

hp = HealPotion("Health Potion", "Healing Flower", True)
hp.heal()

stamina = StaminaPotion("Stamina Potion", "Stamina Flower", True)
stamina.stamina()

hs = MegaPotion("Mega Potion", "Healing and Stamina Flower", True)
hs.potion()

my_axe = Axe()
my_axe.swing()

my_Faxe = FasterAxe()
my_Faxe.swing()

my_Longsword = LongSword()
my_Longsword.swing()

my_SLongsword = SLongSword()
my_SLongsword.swing()

my_bow = Bow("Starter Bow", "Wood")
my_bow.shot(4)

my_Wbow = WindBow("Wind Bow", "Wind ore")
my_Wbow.shot(3)

_SpacePart = SpacePart1('1', '2')
print(_SpacePart.combination)

