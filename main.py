from contextlib import closing
import time
import pypot.robot

import socket

from configs.ergo_config import ergo_config
from configs.single_motor_config import single_motor_config
from configs.head_config import head_config
from controllers.basic_controller_template import basic_controller
from controllers.web_controller import WebController


UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


with closing(pypot.robot.from_config(head_config)) as robot:
    robot.start_sync()

    # Put the robot in its initial position
    for m in robot.motors:  # Note that we always provide an alias for all motors.
        m.compliant = False
    #  m.goal_position = 0

    # Wait for the robot to actually reach the base position.
    time.sleep(2)

    # Start robot here
    # basic_controller(robot)
    controller = WebController(robot, sock)
    # controller = basic_controller(robot)

    for m in robot.motors:  # Note that we always provide an alias for all motors.
        m.compliant = True







