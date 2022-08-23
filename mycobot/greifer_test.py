from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
import time


def gripper_test(robot):
    status = robot.is_gripper_moving()
    print(f"gripper status: {status}")
    time.sleep(1)

    robot.set_encoder(1, 2048)
    time.sleep(2)

    robot.set_encoders([1024, 1024, 1024, 1024, 1024, 1024], 20)
    time.sleep(3)

    print(f"joint 1: {robot.get_encoder(1)}")
    robot.set_encoder(7, 2048)
    time.sleep(3)

    robot.set_encoder(7, 1300)
    time.sleep(3)


    robot.set_gripper_value(255, 70)
    time.sleep(4)

    for i in range(4):
        robot.set_gripper_state(0, 70)
        time.sleep(3)

        robot.set_gripper_state(1, 70)
        time.sleep(3)

    print(f"\ngripper value: {robot.get_gripper_value()}")


if __name__ == "__main__":
    robot = MyCobot(PI_PORT,  PI_BAUD)
    robot.set_encoders([2048, 2048, 2048, 2048, 2048, 2048], 20)
    time.sleep(3)
    gripper_test(robot)
