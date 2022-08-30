from Flys import FlyBehavior, FlyNoWay, FlyWithWings, FlyRocketPowered
from Quacks import Quack, QuackBehavior, MuteQuack, Squeak


class Duck:

    def __init__(self):
        print("Я родился")
        self.quackBehavior = QuackBehavior()
        self.flyBehavior = FlyBehavior()

    def swim(self):
        print("Я плаваю")

    def display(self):
        pass

    def performFly(self):
        self.flyBehavior.fly()

    def performQuack(self):
        self.quackBehavior.quack()


class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.quackBehavior = Quack()
        self.flyBehavior = FlyWithWings()

    def display(self):
        print("I'm real Mallard duck")


class ModelDuck(Duck):
    def __init__(self):
        super().__init__()
        self.flyBehavior = FlyNoWay()
        self.quackBehavior = MuteQuack()

    def display(self):
        print("I'm a model duck")





