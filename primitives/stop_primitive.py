import numpy
from easingutilities.easing.SinusoidalEase import SinusoidalEase
from easingutilities.easingcontroller.EasingController import EasingController
import pypot.primitive


class StopPrimitive(pypot.primitive.LoopPrimitive):
    def __init__(self, robot, steps, freq=1000):
        self.robot = robot

        self.left_right_controller = EasingController(robot.left_right, SinusoidalEase, steps)
        self.left_right_controller.goal = 70
        self.left_right_controller.__iter__()

        self.knee_controller = EasingController(robot.knee, SinusoidalEase, steps)
        self.knee_controller.goal = -10
        self.knee_controller.__iter__()

        pypot.primitive.LoopPrimitive.__init__(self, robot, freq)

    # The update function is automatically called at the frequency given on the constructor
    def update(self):
        try:
            print("moves motor")
            self.robot.left_right.goal_position = self.left_right_controller.__next__()
            self.robot.knee.goal_position = self.knee_controller.__next__()
        except StopIteration:
            print("Stops iterator")
            self.stop()
