from microbit import *
from Cutebot import *
import random
import music

ct = CUTEBOT()


centering = False

forward_direction_check_rotation_speed = 30;
direction_check_rotation_speed = 35;
rotation_speed = 30;
forward_speed = 30;
correct_tracking_left = (20, 40)
correct_tracking_right = (40, 20)

while True:
    tracking = ct.get_tracking()

    if centering:
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
            music.play("C4:1")

        # Left on black, right on white - veer left
        elif forward_tracking == 10:
            valid_headings.append('forward')
            while ct.get_tracking() != 11:
                ct.set_motors_speed(-forward_direction_check_rotation_speed, forward_direction_check_rotation_speed)
            ct.set_motors_speed(0, 0)
            music.play("C4:1")

        elif forward_tracking == 11:
            valid_headings.append('forward')
            music.play("C4:1")

        sleep(250)

        # Check if left is possible (rotate left up to 400ms or until line is found)
        start_time = running_time()
        ct.set_motors_speed(-direction_check_rotation_speed, direction_check_rotation_speed)
        sleep(200)

        while running_time() - start_time < 400:
            if ct.get_tracking() == 11:
                valid_headings.append('left')
                music.play("C4:1")
                break

        elapsed = running_time() - start_time
        ct.set_motors_speed(0, 0)
        sleep(250)

        # Re-center if line wasn't found (rotate back same amount of time)
        ct.set_motors_speed(direction_check_rotation_speed, -direction_check_rotation_speed)
        sleep(elapsed)
        ct.set_motors_speed(0, 0)
        sleep(250)

        # Check if right is possible.
        start_time = running_time()
        ct.set_motors_speed(direction_check_rotation_speed, -direction_check_rotation_speed)
        sleep(200)

        while running_time() - start_time < 400:
            if ct.get_tracking() == 11:
                valid_headings.append('right')
                music.play("C4:1")
                break

        elapsed = running_time() - start_time
        ct.set_motors_speed(0, 0)
        sleep(250)

        # Re-center if line wasn't found (rotate back same amount of time)
        ct.set_motors_speed(-direction_check_rotation_speed, direction_check_rotation_speed)
        sleep(elapsed)
        ct.set_motors_speed(0, 0)
        sleep(250)

        if len(valid_headings) == 0:
            valid_headings.append('return')

        #Choose random direction
        direction = random.choice(valid_headings)

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
            ct.set_motors_speed(0, 0)
            sleep(100)
            ct.set_motors_speed(-rotation_speed, rotation_speed)
            while ct.get_tracking() != 11:
                ct.set_motors_speed(-rotation_speed, rotation_speed);
            ct.set_motors_speed(0, 0)
            sleep(100)

        if direction == 'forward':
            sleep(100)

        centering = False

    elif tracking == 11:
        # Both sensors on black - go straight
        ct.set_motors_speed(forward_speed, forward_speed)

    elif tracking == 10:
        # Left on black, right on white - veer left
        left_speed, right_speed = correct_tracking_left
        ct.set_motors_speed(left_speed, right_speed)

    elif tracking == 1:
        left_speed, right_speed = correct_tracking_right
        ct.set_motors_speed(left_speed, right_speed)

        # Left on white, right on black - veer right
        ct.set_motors_speed(left_speed, right_speed)

    elif tracking == 0:
        # Both sensors on white - lost line
        sleep(200)
        ct.set_motors_speed(0, 0)
        centering = True