class Item(object):
    def __init__(self, name, material):
        self.name = name
        self.material = material


class Sword(Item):
    def __init__(self, name, material, dmg=20):
        super(Sword, self).__init__(name, material)
        self.equip = True
        self.use = False
        self.dmg = dmg

    def hold(self):
        self.equip = True
        print("You have %s equipped." % self.name)

    def swing(self):
        self.use = True
        print("You start swinging your sword.")

    def stop(self):
        self.use = False
        print("You stopped using the %s" % self.name)


class FireSword(Sword):
    def __init__(self, name, material, shoot=False, dmg=35):
        super(FireSword, self).__init__(name, material)
        self.shoot = shoot
        self.ammo = 5
        self.dmg = dmg

    def fireball(self, shots):
        if self.shoot:
            if self.ammo <= 0:
                print("You need to reload.")
            elif self.ammo < shots:
                print("You shot %s fireball and ran out." % self.ammo)
                self.ammo = 0
            else:
                print("You shoot %s fireball." % self.ammo)
                self.ammo -= shots
        else:
            print("You can't shoot.")

    def reload(self):
        self.ammo = 5
        print("Your fire sword is fully charged.")


class LightningSword(Sword):
    def __init__(self, name, material, shoot=False, dmg=45):
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
                print("You shoot %s lightning bolt." % self.ammo)
                self.ammo -= shots
        else:
            print("You can't shoot.")

    def reload(self):
        self.ammo = 5
        print("Your lightning sword is fully charged.")


class WindSword(Sword):
    def __init__(self, name, material, shoot=False, dmg=25):
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
                print("You blew %s gust of wind." % self.ammo)
                self.ammo -= shots
        else:
            print("You can't shoot.")

    def reload(self):
        self.ammo = 5
        print("Your wind sword is fully charged.")


class WaterSword(Sword):
    def __init__(self, name, material, shoot=False, dmg=25):
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
                print("You shoot %s water bullet." % self.ammo)
                self.ammo -= shots
        else:
            print("You can't shoot.")

    def reload(self):
        self.ammo = 5
        print("Your water sword is fully charged.")


class EarthSword(Sword):
    def __init__(self, name, material, shoot=False, dmg=30):
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
                print("You shoot %s block of rock." % self.ammo)
                self.ammo -= shots
        else:
            print("You can't shoot.")

    def reload(self):
        self.ammo = 5
        print("Your earth sword is fully charged.")


class Bow(Item):
    def __init__(self, name, material, shoot=False):
        super(Bow, self).__init__(name, material)
        self.shoot = shoot
        self.arrow = 10
        self.dmg = 20

    def shoot(self, shots):
        if self.shoot:
            if self.arrow <= 0:
                print("You need to reload.")
            elif self.arrow < shots:
                print("You shot %s arrow and ran out." % self.arrow)
            else:
                print("You shoot %s arrow." % self.arrow)
                self.arrow -= shots
        else:
            print("You can't shoot.")

    def reload(self):
        self.arrow = 10
        print("You reloaded your arrows.")


class WindBow(Item):
    def __init__(self, name, material, shoot=False):
        super(WindBow, self).__init__(name, material)
        self.shoot = shoot
        self.arrow = 12
        self.dmg = 25
        self.knockback = 30

    def shoot(self, shots):
        if self.shoot:
            if self.arrow <= 0:
                print("You need to reload.")
            elif self.arrow < shots:
                print("You shot %s wind arrow and ran out." % self.arrow)
            if self.shoot:
                print("You knocked the target back.")
            else:
                print("You shoot %s wind arrow." % self.arrow)
                self.arrow -= shots
        else:
            print("You can't shoot.")

    def reload(self):
        self.arrow = 10
        print("You reloaded your arrows.")


class Axe(Sword):
    def __init__(self):
        super(Axe, self).__init__("Starter Axe", "Metal")
        self.chopspeed = 20


class FasterAxe(Sword):
    def __init__(self):
        super(FasterAxe, self).__init__("Faster Axe", "Speed ore")
        self.chopspeed = 35


class LongSword(Sword):
    def __init__(self):
        super(LongSword, self).__init__("Long Sword", "Metal")
        self.dmg = 25


class SLongSword(Sword):
    def __init__(self):
        super(SLongSword, self).__init__("Steel LongSword", "Steel")
        self.dmg = 35


class HealPotion(Item):
    def __init__(self, name, material):
        super(HealPotion, self).__init__(name, material)
        self.heal = 50

    def heal(self):
        if self.heal:
            print("You heal 50 hp.")


class StaminaPotion(Item):
    def __init__(self, name, material):
        super(StaminaPotion, self).__init__(name, material)
        self.stamina = 50

    def stamina(self):
        if self.stamina:
            print("You gained 50 stamina")


class MegaPotion(Item):
    def __init__(self, name, material):
        super(MegaPotion, self).__init__(name, material)
        self.potion = 50

    def potion(self):
        if self.potion:
            print("You gained 50 stamina and health")


my_sword = Sword("Starter sword", "Metal")
my_sword.swing()

my_Fsword = FireSword("Fire Sword", "Flame Ore")
my_Fsword.fireball(3)

my_Lsword = LightningSword("Linghtning Sword", "Lightning Ore")
my_Lsword.lightning(5)

my_Wsword = WaterSword("Water Sword", "Water Ore")
my_Wsword.water(2)

my_Esword = EarthSword("Earth Sword", "Earth Ore")
my_Esword.swing()

my_WIsword = WindSword("Wind Sword", "Earth Ore")
my_WIsword.wind(3)

my_hp = HealPotion("Health Potion", "Healing Flower")
my_hp.heal()

my_stamina = StaminaPotion("Stamina Potion", "Stamina Flower")
my_stamina.stamina()

my_hs = MegaPotion("Mega Potion", "Healing and Stamina Flower")
my_hs.potion()

my_axe = Axe
my_axe.swing()

my_Faxe = FasterAxe
my_Faxe.swing()

my_Longsword = LongSword
my_Longsword.swing()

my_SLongsword = SLongSword
my_SLongsword.swing()

my_bow = Bow("Starter Bow", "Wood")
my_bow.shoot()

