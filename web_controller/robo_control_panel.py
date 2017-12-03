from flask import Flask
from flask import render_template
from subprocess import Popen, PIPE
import time

app = Flask(__name__)

proc = Popen(["python", "print_test.py"],
             stdin=PIPE)


@app.route("/")
def control_panel():
        return render_template('controlPanel.html')


@app.route("/pose/<a_pose>", methods=['PUT'])
def pose(a_pose=None):
        message = "hottie"
        encoded_message = message.encode()
        time.sleep(5)
        print(str(encoded_message))
        print('result:', proc.stdin.write(encoded_message))
        proc.stdin.flush()
        return '200'


