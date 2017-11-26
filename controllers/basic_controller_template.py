from primitives.basic_primitive_template import EasePrimitive
import time


def basic_controller(robot):
    ease = EasePrimitive(robot, 50)
    ease.start()
    time.sleep(30)