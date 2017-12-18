from easingutilities.easing.BounceEase import BounceEase
from easingutilities.easingcontroller.EasingController import EasingController
import pypot.primitive


class MainPositionPrimitive(pypot.primitive.LoopPrimitive):
    def __init__(self, robot, refresh_freq, amp=30, freq=0.5,):
        self.robot = robot
        self.amp = amp
        self.freq = freq
        self.up_down_controller = EasingController(robot.up_down, BounceEase, 1000)
        self.up_down_controller.goal = 0
        self.up_down_controller.__iter__()
        self.left_right_controller = EasingController(robot.left_right)
        self.left_right_controller.goal = 0
        self.left_right_controller.__iter__()
        pypot.primitive.LoopPrimitive.__init__(self, robot, refresh_freq)

    # The update function is automatically called at the frequency given on the constructor
    def update(self):
        try:
            # print("moves motor")
            next_step = self.up_down_controller.__next__()
            self.robot.up_down.goal_position = next_step
        except StopIteration:
            print("Head stops iterator")
            self.stop()

        try:
            # print("moves motor")
            next_step = self.left_right_controller.__next__()
            self.robot.left_right.goal_position = next_step
        except StopIteration:
            print("base stops iterator")
            self.stop()







