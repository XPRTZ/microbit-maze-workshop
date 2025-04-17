from direction import Direction
from microbit import *
from cutebot import *

ct = CUTEBOT()

SLEEP_TURN_PAUSE_TIME=400
LEFT_SPEED = 29
RIGHT_SPEED = 30

hasTurnedLeft = False
hasTurnedRight = False

def headlights():
    WHITE = (255, 255, 255)
    ct.set_car_light(left, WHITE[0], WHITE[1], WHITE[2])
    ct.set_car_light(right, WHITE[0], WHITE[1], WHITE[2])

def stop():
    ct.set_motors_speed(0, 0)

def drive():
    ct.set_motors_speed(LEFT_SPEED, RIGHT_SPEED)

def turnAndDrive():
    turnLeft()
    if impendingCollision:
        turnLeft()
    drive()

def impendingCollision():
    dist = ct.get_distance()
    return dist> 1 and dist < 10

def turnLeft():
    ct.set_motors_speed(-LEFT_SPEED, RIGHT_SPEED)
    sleep(SLEEP_TURN_PAUSE_TIME)

def turnRight():
    ct.set_motors_speed(LEFT_SPEED, -RIGHT_SPEED)
    sleep(SLEEP_TURN_PAUSE_TIME)
    
headlights()
while True:
    if not impendingCollision():
        drive()

    if impendingCollision():
        turnAndDrive()

    # if impendingCollision():
    #     if not hasTurnedLeft:
    #         turnLeft()
    #         hasTurnedLeft = True
    #     if not hasTurnedRight:
    #         turnRight()
    #         hasTurnedRight = True
    #     if not hasTurnedLeft and not hasTurnedRight:
    #         turnLeft()
    #         turnRight()
    #         hasTurnedLeft = True
    #         hasTurnedRight = SLEEP_TURN_PAUSE_TIME
    #     drive()
    #     hasTurnedRight = False
    #     hasTurnedLeft = False