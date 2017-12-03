from subprocess import Popen, PIPE
import time

proc = Popen(["python", "print_something.py"],
             stdin=PIPE)
message = "hottie"
encoded_message = message.encode()
time.sleep(5)
print(str(encoded_message))
print('result:', proc.stdin.write(encoded_message))
proc.stdin.flush()

