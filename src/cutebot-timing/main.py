from microbit import *
from cutebot import *


ct = CUTEBOT()

#Speed values and timing values
SPEED = 35
DRIVE_WHILE_LOST_LINE_TIME = 150
CORRECT_TRACKING_LEFT = (SPEED-10, SPEED+10)
CORRECT_TRACKING_RIGHT = (SPEED+10, SPEED-10)
MAX_DIRECTION_CHECK_TIME = 400
DIRECTION_CHECK_DELAY = 200

#Line sensor
LEFT_BLACK_RIGHT_WHITE = 10
LEFT_WHITE_RIGHT_BLACK = 1
LEFT_BLACK_RIGHT_BLACK = 11
LEFT_WHITE_RIGHT_WHITE = 0

#Directions
LEFT = 0
RIGHT = 1
FORWARD = 2
RETURN = 3

# Blink light function
def blink_light(left_rgb, right_rgb, times=1, interval=200):
    left = 0x04
    right = 0x08

    for _ in range(times):
        ct.set_car_light(left, *left_rgb)
        ct.set_car_light(right, *right_rgb)
        sleep(interval)
        ct.set_car_light(left, 0, 0, 0)
        ct.set_car_light(right, 0, 0, 0)
        sleep(interval)

# Function to calculate absolute angle difference
def absolute_angle_difference(start, end):
    return abs(end - start)

def turn(turn_speed):
    ct.set_motors_speed(*turn_speed)
    sleep(DIRECTION_CHECK_DELAY)

    while ct.get_tracking() != 11:
        continue

    ct.set_motors_speed(0, 0);

# Function to check direction
def check_direction(direction_name, turn_speed, return_speed, angle_delta=80):
    valid = False

    start_time = running_time()

    # Start turning
    ct.set_motors_speed(*turn_speed)
    sleep(DIRECTION_CHECK_DELAY)

    while running_time() - start_time < MAX_DIRECTION_CHECK_TIME:
        tracking = ct.get_tracking()
        if direction_name == LEFT and tracking in (LEFT_BLACK_RIGHT_WHITE, LEFT_BLACK_RIGHT_BLACK):
            valid = True
            break
        elif direction_name == RIGHT and tracking in (LEFT_WHITE_RIGHT_BLACK, LEFT_BLACK_RIGHT_BLACK):
            valid = True
            break

    elapsed = running_time() - start_time
    ct.set_motors_speed(0, 0)
    sleep(250)

    # Re-center
    ct.set_motors_speed(*return_speed)
    sleep(elapsed)
    ct.set_motors_speed(0, 0)
    sleep(250)

    # Visual feedback
    if direction_name == LEFT:
        blink_light((0, 255, 0), (0, 0, 0)) if valid else blink_light((255, 0, 0), (0, 0, 0))
    elif direction_name == RIGHT:
        blink_light((0, 0, 0), (0, 255, 0)) if valid else blink_light((0, 0, 0), (255, 0, 0))

    return valid

def can_drive_forward():
    tracking = ct.get_tracking()
    if tracking == LEFT_BLACK_RIGHT_BLACK:
        ct.set_motors_speed(SPEED, SPEED)

    elif tracking == LEFT_BLACK_RIGHT_WHITE:
        left_speed, right_speed = CORRECT_TRACKING_LEFT
        ct.set_motors_speed(left_speed, right_speed)

    elif tracking == LEFT_WHITE_RIGHT_BLACK:
        left_speed, right_speed = CORRECT_TRACKING_RIGHT
        ct.set_motors_speed(left_speed, right_speed)

    elif tracking == LEFT_WHITE_RIGHT_WHITE:
        sleep(DRIVE_WHILE_LOST_LINE_TIME)
        ct.set_motors_speed(0, 0)
        return False

    return True

def turn_until_on_line(left_speed, right_speed):
    initial_tracking = ct.get_tracking()

    # Step 1: Turn until tracking changes
    ct.set_motors_speed(left_speed, right_speed)
    while ct.get_tracking() == initial_tracking:
        sleep(5)

    # Step 2: Continue until on the correct line
    while ct.get_tracking() != LEFT_BLACK_RIGHT_BLACK:
        sleep(5)

    ct.set_motors_speed(0, 0)

def realign_forward_if_tracking_is_partial():
    if forward_tracking == LEFT_WHITE_RIGHT_BLACK:
        ct.set_motors_speed(SPEED, -SPEED)
    elif forward_tracking == LEFT_BLACK_RIGHT_WHITE:
        ct.set_motors_speed(-SPEED, SPEED)
    else:
        return False  # No correction needed can't go forward

    while ct.get_tracking() != LEFT_BLACK_RIGHT_BLACK:
        continue

    ct.set_motors_speed(0, 0)

    return True

while True:
    tracking = ct.get_tracking()

    can_drive = can_drive_forward()

    if can_drive == False:
        valid_headings = []
        sleep(250)
        forward_tracking = ct.get_tracking()

        if realign_forward_if_tracking_is_partial() is True:
            valid_headings.append(FORWARD)
            blink_light((0, 255, 0), (0, 255, 0))  # green both
        else:
            blink_light((255, 0, 0), (255, 0, 0))  # red both

        sleep(250)

        left_result = check_direction(LEFT, (-SPEED, SPEED), (SPEED, -SPEED))
        right_result = check_direction(RIGHT, (SPEED, -SPEED), (-SPEED, SPEED))

        if left_result: valid_headings.append(LEFT)
        if right_result: valid_headings.append(RIGHT)

        # Default direction is return
        direction = RETURN

        if FORWARD in valid_headings:
            sleep(100)
        elif RIGHT in valid_headings:
            turn_until_on_line(SPEED, -SPEED)
            sleep(100)
        elif LEFT in valid_headings:
            turn_until_on_line(-SPEED, SPEED)
            sleep(100)
        else:
            turn_until_on_line(SPEED, -SPEED)
            sleep(100)