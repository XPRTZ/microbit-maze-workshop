from microbit import *
from Cutebot import *

ct = CUTEBOT()

choose_direction = False

#Can be used with "normal" battery.
forward_direction_check_rotation_speed = 30;
direction_check_rotation_speed = 35;
direction_check_rotation_time = 400;
direction_check_leave_time = 200;
rotation_speed = 30;
forward_speed = 30;
correct_tracking_left = (20, 40)
correct_tracking_right = (40, 20)
sleep_when_lost_line_time = 150;

#Can be used with "high" battery.
#forward_direction_check_rotation_speed = 25;
#direction_check_rotation_speed = 30;
#direction_check_rotation_time = 350;
#direction_check_leave_time = 200;
#rotation_speed = 25;
#forward_speed = 25;
#correct_tracking_left = (15, 30)
#correct_tracking_right = (30, 15)
#sleep_when_lost_line_time = 100;

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

def check_direction(direction_name, turn_speed, return_speed):
    valid = False
    start_time = running_time()
    ct.set_motors_speed(*turn_speed)
    sleep(direction_check_leave_time)

    while running_time() - start_time < direction_check_rotation_time:
        tracking = ct.get_tracking()
        if direction_name == 'left' and tracking in (10, 11):
            valid = True
            break
        elif direction_name == 'right' and tracking in (1, 11):
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

    if direction_name == "left":
        if valid:
            blink_light((0, 255, 0), (0, 0, 0))  # green left
        else:
            blink_light((255, 0, 0), (0, 0, 0))  # red left

    elif direction_name == "right":
        if valid:
            blink_light((0, 0, 0), (0, 255, 0))  # green right
        else:
            blink_light((0, 0, 0), (255, 0, 0))  # red right

    return direction_name if valid else None

while True:
    tracking = ct.get_tracking()

    if choose_direction:
        # Move forward briefly to try finding the line
        sleep(250)

        valid_headings = [];

        forward_tracking = ct.get_tracking();

        # Left on white, right on black - veer right
        if forward_tracking == 1:
            valid_headings.append('forward')
            while ct.get_tracking() != 11:
                ct.set_motors_speed(forward_direction_check_rotation_speed, -forward_direction_check_rotation_speed)
            ct.set_motors_speed(0, 0)

        # Left on black, right on white - veer left
        elif forward_tracking == 10:
            valid_headings.append('forward')
            while ct.get_tracking() != 11:
                ct.set_motors_speed(-forward_direction_check_rotation_speed, forward_direction_check_rotation_speed)
            ct.set_motors_speed(0, 0)

        elif forward_tracking == 11:
            valid_headings.append('forward')

        if 'forward' in valid_headings:
            blink_light((0, 255, 0), (0, 255, 0))  # green both
        else:
            blink_light((255, 0, 0), (255, 0, 0))  # red both

        sleep(250)

        left = check_direction('left', (-direction_check_rotation_speed, direction_check_rotation_speed),
                              (direction_check_rotation_speed, -direction_check_rotation_speed));

        right = check_direction('right', (direction_check_rotation_speed, -direction_check_rotation_speed),
                                        (-direction_check_rotation_speed, direction_check_rotation_speed));

        if left: valid_headings.append(left)
        if right: valid_headings.append(right)

        direction = 'return'

        if 'forward' in valid_headings:
            direction = 'forward';

        elif 'right' in valid_headings:
            direction = 'right';

        elif 'left' in valid_headings:
            direction = 'left';

        if direction == 'left':
            ct.set_motors_speed(-rotation_speed, rotation_speed)
            sleep(200)
            while ct.get_tracking() != 11:
                ct.set_motors_speed(-rotation_speed, rotation_speed);
            ct.set_motors_speed(0, 0);

        if direction == 'right':
            ct.set_motors_speed(rotation_speed, -rotation_speed)
            sleep(200)
            while ct.get_tracking() != 11:
                ct.set_motors_speed(rotation_speed, -rotation_speed);
            ct.set_motors_speed(0, 0);

        if direction == 'return':
            ct.set_motors_speed(-rotation_speed, -rotation_speed)
            sleep(100)
            ct.set_motors_speed(-rotation_speed, rotation_speed)
            sleep(100)
            while ct.get_tracking() != 11:
                ct.set_motors_speed(-rotation_speed, rotation_speed);
            ct.set_motors_speed(0, 0)
            sleep(100)

        if direction == 'forward':
            sleep(100)

        choose_direction = False

    elif tracking == 11:
        # Both sensors on black - go straight
        ct.set_motors_speed(forward_speed, forward_speed)

    elif tracking == 10:
        # Left on black, right on white - veer left
        left_speed, right_speed = correct_tracking_left
        ct.set_motors_speed(left_speed, right_speed)

    elif tracking == 1:
        left_speed, right_speed = correct_tracking_right

        # Left on white, right on black - veer right
        ct.set_motors_speed(left_speed, right_speed)

    elif tracking == 0:
        # Both sensors on white - lost line
        sleep(sleep_when_lost_line_time)
        ct.set_motors_speed(0, 0)
        choose_direction = True