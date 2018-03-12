import pickle

from primitives.main_position_primitive import MainPositionPrimitive
from primitives.easing_primitive import EasePrimitive
from primitives.go_to_position_primitive import GoToPositionPrimitive
from primitives.bow_primitive import BowPrimitive
from primitives.stop_primitive import StopPrimitive


class WebController:
    def __init__(self, robot, sock):
        self.robot = robot
        print('Web controller is running!')
        self.left_right_position = GoToPositionPrimitive(self.robot, 'left_right', 0, 1000)
        self.up_down_position = GoToPositionPrimitive(self.robot, 'up_down', 0, 1000)
        self.rotation_position = GoToPositionPrimitive(self.robot, 'rotation', 0, 1000)
        self.knee_position = GoToPositionPrimitive(self.robot, 'knee', 0, 1000)

        while True:
            data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
            pose_info = pickle.loads(data)
            #  pose_info = data.decode("utf-8")
            print("received message:", pose_info)
            if pose_info['pose'] == "hottie":
                self.ease_move()
            if pose_info['pose'] == "main_position":
                self.main_position()
            if pose_info['pose'] == "break":
                break
            if pose_info['pose'] == "bow":
                self.bow()
            if pose_info['pose'] == 'stop':
                self.stop()
            if pose_info['pose'] == "to_position":
                if pose_info['motor'] == 'up_down':
                    self.up_down_to_position(float(int(pose_info['pos'])))  # Convert string to int
                if pose_info['motor'] == 'left_right':
                    self.left_right_to_position(float(int(pose_info['pos'])))  # Convert string to int
                if pose_info['motor'] == 'rotation':
                    self.rotation_to_position(float(int(pose_info['pos'])))  # Convert string to int
                if pose_info['motor'] == 'knee':
                    self.knee_to_position(float(int(pose_info['pos'])))  # Convert string to int

    def ease_move(self):
        ease = EasePrimitive(self.robot, 1000, 10000, 60)
        ease.start()

    def main_position(self):
        move = MainPositionPrimitive(self.robot, 1000)
        move.start()

    def bow(self):
        move = BowPrimitive(self.robot, 3500, 1500)
        move.start()

    def stop(self):
        move = StopPrimitive(self.robot, 4000, 1500)
        move.start()

    def left_right_to_position(self, pos):
        self.left_right_position.stop()
        self.left_right_position = GoToPositionPrimitive(self.robot, 'left_right', pos, 1000)
        self.left_right_position.start()

    def up_down_to_position(self, pos):
        self.up_down_position.stop()
        self.up_down_position = GoToPositionPrimitive(self.robot, 'up_down', pos, 1000)
        self.up_down_position.start()

    def rotation_to_position(self, pos):
        self.rotation_position.stop()
        self.rotation_position = GoToPositionPrimitive(self.robot, 'rotation', pos, 1000)
        self.rotation_position.start()

    def knee_to_position(self, pos):
        self.knee_position.stop()
        self.knee_position = GoToPositionPrimitive(self.robot, 'knee', pos, 1000)
        self.knee_position.start()
