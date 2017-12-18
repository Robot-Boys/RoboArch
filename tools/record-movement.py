import time
import pypot.robot

from pypot.primitive.move import MoveRecorder, Move, MovePlayer
#  Todo: Import is not working in runtime
from configs.ergo_config import ergo_config

robot = pypot.robot.from_config(ergo_config)

move_recorder = MoveRecorder(robot, 50, robot.motors)

robot.compliant = True
print("start recording..")
move_recorder.start()
time.sleep(5)
print("Recording end.")
move_recorder.stop()

with open('my_nice_move.move', 'w') as f:
    move_recorder.move.save(f)

with open('my_nice_move.move') as f:
    m = Move.load(f)

robot.compliant = False

print("Play recording")
move_player = MovePlayer(robot, m)
move_player.start()
time.sleep(10)
print("recording played")

