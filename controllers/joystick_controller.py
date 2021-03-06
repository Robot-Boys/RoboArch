import pickle
from primitives.joystick_primitive import JoystickPrimitive
from primitives.bow_primitive import BowPrimitive


class JoystickController:
    def __init__(self, robot, sock):
        self.robot = robot
        print('joystick controller is running!')
        self.pitch = JoystickPrimitive(self.robot, 'up_down', 0, 1000)
        self.yaw = JoystickPrimitive(self.robot, 'left_right', 0, 1000)
        self.knee = JoystickPrimitive(self.robot, 'knee', 0, 1000)


        while True:
            data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
            info = pickle.loads(data)
            print("received message:", info)
            if 'action' in info:
                # dictionary as switch
                {
                    'PITCH': lambda action: self.move_pitch(action),
                    'YAW': lambda action: self.move_yaw(action),
                    'ROLL': lambda action: self.move_roll(action),
                    'HEIGHT': lambda action: self.move_height(action),
                    'ROTATION': lambda action: self.move_rotation(action),
                    'BOW': lambda action: self.bow(),
                }[info['motor']](float(int(info['action'])))# Convert string to int

    def move_pitch(self, action):
        print('move pitch!', action)
        if self.pitch.state == action:
            return
        self.pitch.stop()
        self.pitch = JoystickPrimitive(self.robot, 'up_down', action, 1000)
        self.pitch.start()

    def move_yaw(self, action):
        print('move yaw!')
        if self.yaw.state == action:
            return
        self.yaw.stop()
        self.yaw = JoystickPrimitive(self.robot, 'left_right', action, 1000)
        self.yaw.start()

    def move_roll(self, action):
        print('move roll!')

    def move_height(self, action):
        print('move Knee!')
        if self.knee.state == action:
            return
        self.knee.stop()
        self.knee = JoystickPrimitive(self.robot, 'knee', action, 1000, 200)
        self.knee.start()

    def move_rotation(self, action):
        print('move rotation!')

    def bow(self):
        move = BowPrimitive(self.robot, 3500, 1500)
        move.start()
