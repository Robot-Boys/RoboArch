from contextlib import closing
import time
import pypot.robot

import socket

from configs.ergo_config import ergo_config
from configs.single_motor_config import single_motor_config
from configs.lamp_config import lamp_config
from controllers.basic_controller_template import basic_controller
from controllers.web_controller import WebController
from controllers.joystick_controller import JoystickController


UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

print("going on")

with closing(pypot.robot.from_config(lamp_config)) as robot:
    robot.start_sync()

    # Put the robot in its initial position
    for m in robot.motors:  # Note that we always provide an alias for all motors.
        m.compliant = False
    #  m.goal_position = 0

    # Wait for the robot to actually reach the base position.
    time.sleep(2)

    # controller = basic_controller(robot)

    # Start robot here
    # basic_controller(robot)
    controller = JoystickController(robot, sock)


    for m in robot.motors:  # Note that we always provide an alias for all motors.
        m.compliant = True







