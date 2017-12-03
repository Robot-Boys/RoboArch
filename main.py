import sys
from contextlib import closing
import time


import pypot.robot

from configs.ergo_config import ergo_config
from controllers.basic_controller_template import basic_controller
from controllers.web_controller import WebController
controller = None

with closing(pypot.robot.from_config(ergo_config)) as robot:
    robot.start_sync()

    # Put the robot in its initial position
    for m in robot.motors:  # Note that we always provide an alias for all motors.
        m.compliant = False
        m.goal_position = 0

    # Wait for the robot to actually reach the base position.
    time.sleep(2)

    # Start robot here
    # basic_controller(robot)
    controller = WebController(robot)





