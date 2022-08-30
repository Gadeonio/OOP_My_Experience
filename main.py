from Ducks import MallardDuck, Duck, ModelDuck
from Flys import FlyRocketPowered

if __name__=="__main__":

    RobotDuck = ModelDuck()
    RobotDuck.performFly()
    RobotDuck.flyBehavior = FlyRocketPowered()
    RobotDuck.performFly()