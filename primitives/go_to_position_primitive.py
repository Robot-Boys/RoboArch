from easingutilities.easing.LinearEase import LinearEase
from easingutilities.easing.SinusoidalEase import SinusoidalEase
from easingutilities.easing.BackEase import BackEase
from easingutilities.easing.BounceEase import BounceEase
from easingutilities.easingcontroller.EasingController import EasingController
import pypot.primitive


class GoToPositionPrimitive(pypot.primitive.LoopPrimitive):
    def __init__(self, robot, motor_id, pos, steps, freq=1000):
        self.robot = robot
        self.motor = getattr(self.robot, motor_id)
        self.freq = freq
        self.controller = EasingController(self.motor, BounceEase(), steps)
        #self.controller = EasingController(self.motor, BackEase(), steps)
        #self.controller = EasingController(self.motor, SinusoidalEase, steps)
        self.controller.goal = pos
        self.controller.__iter__()
        print('Go to posisiont: ', motor_id, pos)
        pypot.primitive.LoopPrimitive.__init__(self, robot, freq)

    # The update function is automatically called at the frequency given on the constructor
    def update(self):
        try:
            print("moves motor")
            next_step = self.controller.__next__()
            self.motor.goal_position = next_step
        except StopIteration:
            print("Stops iterator")
            self.stop()
