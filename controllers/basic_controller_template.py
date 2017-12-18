from primitives.easing_primitive import EasePrimitive
import time


def basic_controller(robot):
    ease = EasePrimitive(robot, 1000, 10000, 60)
    ease.start()
    time.sleep(30)
    ease= EasePrimitive(robot, 1000, 10000, -60)
    ease.start()
    time.sleep(30)
