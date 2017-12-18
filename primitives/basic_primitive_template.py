import numpy
from mocks.movement_iterator_mock import EaseCounter
import pypot.primitive


class EaseTemplatePrimitive(pypot.primitive.LoopPrimitive):
    def __init__(self, robot, refresh_freq, amp=30, freq=0.5):
        self.robot = robot
        self.amp = amp
        self.freq = freq
        t = numpy.arange(0, 10, 0.01)
        speeds = amp * numpy.cos(2 * numpy.pi * freq * t)
        self.easeCounter = EaseCounter(speeds)
        pypot.primitive.LoopPrimitive.__init__(self, robot, refresh_freq)

    # The update function is automatically called at the frequency given on the constructor
    def update(self):
        try:
            # print("moves motor")
            next_step = self.easeCounter.next()
            self.robot.base_pan.goal_speed = next_step
        except StopIteration:
            print("Stops iterator")
            self.robot.base_pan.goal_speed = 0
            self.stop()

