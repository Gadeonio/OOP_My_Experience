class Duck:

    def __init__(self):
        print("Я родился")

    def swim(self):
        print("Я плаваю")

    def display(self):
        pass


class Flyable:
    def fly(self):
        pass


class Fly_bird(Flyable):

    def fly(self):
        print("Лечу как птица")


class Quackable:
    def quack(self):
        pass


class Quack_bird(Quackable):
    def quack(self):
        print("Кря")


class MyDuck(Duck, Fly_bird, Quack_bird):
    pass

if __name__=="__main__":
    Donald = MyDuck()
    Donald.quack()
    Donald.fly()
    Donald.swim()