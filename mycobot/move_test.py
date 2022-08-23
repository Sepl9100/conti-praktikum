# https://github.com/elephantrobotics/pymycobot/blob/main/docs/README.md
from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
import time


pos1 = [-1.5, 115, -153, 30, -33, 138]
pos2 = [-1.5, 55, -153, 80, 33, 138]

if __name__ == "__main__":
    robot = MyCobot(PI_PORT, PI_BAUD)

    StartTimer = time.time()
    robot.send_angles(pos1, 80)

    while not robot.is_in_position(pos1, 0):
        robot.resume()
        # move for 500ms
        time.sleep(0.5)

        robot.pause()

        # time out protection
        if time.time() - StartTimer > 3:
            break

    StartTimer = time.time()

    while time.time() - StartTimer < 30:
        robot.send_angles(pos1, 80)
        robot.set_color(0, 0, 50)
        time.sleep(0.7)

        robot.send_angles(pos2, 80)
        robot.set_color(0, 50, 0)
        time.sleep(0.7)


    robot.set_