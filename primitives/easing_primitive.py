from easingutilities.easing.BounceEase import BounceEase
from easingutilities.easingcontroller.EasingController import EasingController
import pypot.primitive


class EasePrimitive(pypot.primitive.LoopPrimitive):
    def __init__(self, robot, steps, freq=0.5, goal=0):
        self.robot = robot
        self.freq = freq
        self.controller = EasingController(robot.left_right, BounceEase(), steps)
        self.controller.goal = goal
        self.controller.__iter__()
        pypot.primitive.LoopPrimitive.__init__(self, robot, freq)

    # The update function is automatically called at the frequency given on the constructor
    def update(self):
        try:
            print("moves motorrr")
            next_step = self.controller.__next__()
            self.robot.left_right.goal_position = next_step
        except StopIteration:
            print("Stops iterator")
            self.stop()




