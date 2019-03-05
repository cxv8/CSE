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
        print("Your fire sword is full.")
