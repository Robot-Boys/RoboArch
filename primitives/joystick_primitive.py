from easingutilities.easing.SinusoidalEase import SinusoidalEase
from easingutilities.easingcontroller.EasingController import EasingController
from easingutilities.easing.SinussoidalEaseOut import ElasticEase as SinusoidalEaseOut
import pypot.primitive


class JoystickPrimitive(pypot.primitive.LoopPrimitive):
    def __init__(self, robot, motor_id, action, steps, freq=1000):
        self.robot = robot
        self.motor = getattr(self.robot, motor_id)
        print('motor position:', self.motor.present_position)
        self.state = action
        settings = {
            -1: {
                'pos': self.motor.angle_limit[0],
                'controller': EasingController(self.motor, SinusoidalEase, steps)
            },
            0: {
                'pos': self.calculate_stop(),
                'controller': EasingController(self.motor, SinusoidalEaseOut, steps)
            },
            1: {
                'pos': self.motor.angle_limit[1],
                'controller': EasingController(self.motor, SinusoidalEase, steps)
            }
        }[action]
        print('Pos:', settings['pos'])
        self.freq = freq
        self.controller = settings['controller']
        self.controller.goal = settings['pos']
        self.controller.__iter__()
        print('Go to posisiont: ', motor_id, settings['pos'])
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

    def calculate_stop(self):
        if self.motor.present_position < self.motor.goal_position:
            return self.motor.present_position + 10
        if self.motor.present_position > self.motor.goal_position:
            return self.motor.present_position - 10
        return self.motor.present_position
