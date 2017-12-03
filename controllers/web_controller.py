from primitives.basic_primitive_template import EasePrimitive
import sys
import time


class WebController:
    def __init__(self, robot):
        self.robot = robot
        print('Web controller is running!')

    def ease_move(self):
        ease = EasePrimitive(self.robot, 50)
        ease.start()
        time.sleep(30)

