import sys

print("I am looping!")
while True:
    data = sys.stdin.readline()
    if str(data) != "":
        print("Here is the data: " + str(data))
    sys.stdout.flush()
