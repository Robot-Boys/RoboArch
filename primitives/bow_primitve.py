import numpy
from easingutilities.easing.SinusoidalEase import SinusoidalEase
from easingutilities.easingcontroller.EasingController import EasingController
import pypot.primitive


class BowPrimitive(pypot.primitive.LoopPrimitive):
    def __init__(self, robot, refresh_freq):
        self.robot = robot

        self.up_down_controller = EasingController(robot.up_down, SinusoidalEase)
        self.up_down_controller.goal = 0
        self.up_down_controller.__iter__()

        self.left_right_controller = EasingController(robot.left_right, SinusoidalEase)
        self.left_right_controller.goal = 0
        self.left_right_controller.__iter__()

        self.rotation_controller = EasingController(robot.rotation, SinusoidalEase)
        self.rotation_controller.goal = 0
        self.rotation_controller.__iter__()

        self.knee_controller = EasingController(robot.knee, SinusoidalEase)
        self.knee_controller.goal = 0
        self.knee_controller.__iter__()

        pypot.primitive.LoopPrimitive.__init__(self, robot, refresh_freq)

    # The update function is automatically called at the frequency given on the constructor
    def update(self):
        try:
            print("moves motor")
            self.robot.up_down.goal_position = self.up_down_controller.__next__()
            self.robot.left_right.goal_position = self.left_right_controller.__next__()
            self.robot.rotation.goal_position = self.rotation_controller.__next__()
            self.robot.knee.goal_position = self.knee_controller.__next__()
        except StopIteration:
            print("Stops iterator")
            self.stop()

