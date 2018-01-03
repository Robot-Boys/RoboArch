from primitives.easing_primitive import EasePrimitive
import time


def basic_controller(robot):
    ease = EasePrimitive(robot, 1000, 10, 50)
    ease.start()
    time.sleep(30)
    ease= EasePrimitive(robot, 1000, 10, -60)
    ease.start()
    time.sleep(30)
