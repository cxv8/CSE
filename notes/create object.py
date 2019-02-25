class ToyCar(object):
    def __init__(self,speed,motion=True,distance=30):
        self.twist = 3
        self.direction = True
        self.speed = speed
        self.motion = motion
        self.distance = distance

    def go(self, motion):
        if self.motion:
            if self.twist <= 0:
                print("There is no twist.")
            elif self.twist < motion:
                print("After %s seconds the car stopped moving." % self.twist)
                self.twist = 0
            else:
                print("The car went for %s seconds." % motion)
                self.twist -= motion
        else:
            print("There is no twist.")

    def reload(self):
        self.twist = 3
        print("You twisted the car 3 times.")


My_car = ToyCar(5,True,30)

My_car.go(2)
My_car.go(2)
My_car.reload()
My_car.go(3)
