class Item(object):
    def __init__(self, name, material):
        self.name = name
        self.material = material


class Sword(Item):
    def __init__(self, name, material):
        super(Sword, self).__init__(name, material)
        self.equip = True
        self.use = False

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
    def __init__(self, name, material, shoot=False):
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
                print("You shoot %s fireball." % self.ammo)
                self.ammo -= shots
        else:
            print("You can't shoot.")

    def reload(self):
        self.ammo = 5
        print("Your fire sword is fully charged.")


class LightningSword(Sword):
    def __init__(self, name, material, shoot=False):
        super(LightningSword, self).__init__(name, material)
        self.shoot = shoot
        self.ammo = 5
        self.dmg = 45

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
    def __init__(self, name, material, shoot=False):
        super(WindSword, self).__init__(name, material)
        self.shoot = shoot
        self.ammo = 5
        self.dmg = 25

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
    def __init__(self, name, material, shoot=False):
        super(WaterSword, self).__init__(name, material)
        self.shoot = shoot
        self.ammo = 5
        self.dmg = 25

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
    def __init__(self, name, material, shoot=False):
        super(EarthSword, self).__init__(name, material)
        self.shoot = shoot
        self.ammo = 5
        self.dmg = 30

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