from microbit import *
from cutebot import *
import random
import music

ct = Cutebot()


centering = False

while True:
    tracking = ct.get_tracking()

    if centering:
        # Move forward briefly to try finding the line
        sleep(500)

        valid_headings = [];

        forward_tracking = ct.get_tracking();

        # Left on white, right on black - veer right
        if forward_tracking == 1:
            valid_headings.append('forward')
            while ct.get_tracking() != 11:
                ct.set_motors_speed(30, -30)
            ct.set_motors_speed(0, 0)
            music.play("C4:1")

        # Left on black, right on white - veer left
        elif forward_tracking == 10:
            valid_headings.append('forward')
            while ct.get_tracking() != 11:
                ct.set_motors_speed(-30, 30)
            ct.set_motors_speed(0, 0)
            music.play("C4:1")

        elif forward_tracking == 11:
            valid_headings.append('forward')
            music.play("C4:1")

        sleep(500)

        # Check if left is possible (rotate left up to 400ms or until line is found)
        start_time = running_time()
        ct.set_motors_speed(-35, 35)
        sleep(200)

        while running_time() - start_time < 400:
            if ct.get_tracking() == 11:
                valid_headings.append('left')
                music.play("C4:1")
                found_line = True
                break

        elapsed = running_time() - start_time
        ct.set_motors_speed(0, 0)
        sleep(500)

        # Re-center if line wasn't found (rotate back same amount of time)
        ct.set_motors_speed(35, -35)
        sleep(elapsed)
        ct.set_motors_speed(0, 0)
        sleep(500)

        # Check if right is possible.
        start_time = running_time()
        ct.set_motors_speed(35, -35)
        sleep(200)

        while running_time() - start_time < 400:
            if ct.get_tracking() == 11:
                valid_headings.append('right')
                music.play("C4:1")
                found_line = True
                break

        elapsed = running_time() - start_time
        ct.set_motors_speed(0, 0)
        sleep(500)

        # Re-center if line wasn't found (rotate back same amount of time)
        ct.set_motors_speed(-35, 35)
        sleep(elapsed)
        ct.set_motors_speed(0, 0)
        sleep(500)

        if len(valid_headings) == 0:
            valid_headings.append('return')

        #Choose random direction
        direction = random.choice(valid_headings)

        if direction == 'left':
            ct.set_motors_speed(-30, 30)
            sleep(200)
            while ct.get_tracking() != 11:
                ct.set_motors_speed(-30, 30);
            ct.set_motors_speed(0, 0);

        if direction == 'right':
            ct.set_motors_speed(30, -30)
            sleep(200)
            while ct.get_tracking() != 11:
                ct.set_motors_speed(30, -30);
            ct.set_motors_speed(0, 0);

        if direction == 'return':
            ct.set_motors_speed(-30, -30)
            sleep(100)
            ct.set_motors_speed(0, 0)
            sleep(100)
            ct.set_motors_speed(-30, 30)
            while ct.get_tracking() != 11:
                ct.set_motors_speed(-35, 35);
            ct.set_motors_speed(0, 0)
            sleep(100)

        if direction == 'forward':
            sleep(100)

        centering = False

    elif tracking == 11:
        # Both sensors on black - go straight
        ct.set_motors_speed(30, 30)

    elif tracking == 10:
        # Left on black, right on white - veer left
        ct.set_motors_speed(20, 40)

    elif tracking == 1:
        # Left on white, right on black - veer right
        ct.set_motors_speed(40, 20)

    elif tracking == 0:
        # Both sensors on white - lost line
        ct.set_motors_speed(30, 30)
        sleep(200)
        ct.set_motors_speed(0, 0)
        centering = True
