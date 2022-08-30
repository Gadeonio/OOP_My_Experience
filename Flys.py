class FlyBehavior:
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):

    def fly(self):
        print("Лечу как птица")


class FlyNoWay(FlyBehavior):

    def fly(self):
        print("Не лечу, потому что не умею")


class FlyRocketPowered(FlyBehavior):

    def fly(self):
        print("I'm flying with a rocket!")