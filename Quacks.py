class QuackBehavior:
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print("Кря")


class Squeak(QuackBehavior):
    def quack(self):
        print("Писк")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("*Гробовое молчание*")