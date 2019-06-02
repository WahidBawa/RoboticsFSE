from pygame import *
clock = time.Clock()
import pygame, serial, time

###################################################################### this is all firmata stuff
import pyfirmata
from pyfirmata import Arduino, util
board = Arduino("/dev/ttyACM1")

iterator = util.Iterator(board)
iterator.start();

FL = 4
BL = 3
FR = 6
BR = 5

board.digital[FL].mode = pyfirmata.SERVO
board.digital[BL].mode = pyfirmata.SERVO
board.digital[FR].mode = pyfirmata.SERVO
board.digital[BR].mode = pyfirmata.SERVO

board.digital[FL].write(90)
board.digital[BL].write(90)
board.digital[FR].write(90)
board.digital[BR].write(90)
######################################################################

screen = display.set_mode([500, 700])

init()
joystick.init()


running = True
while running:
	for evt in event.get():
		if evt.type == QUIT:
			running = False

	joystick = pygame.joystick.Joystick(0)
	joystick.init()

	cross_button = joystick.get_button(0)
	circle_button = joystick.get_button(1)
	triangle_button = joystick.get_button(2)
	square_button = joystick.get_button(3)

	left_analog_x = joystick.get_axis(0) * -90
	left_analog_y = joystick.get_axis(1) * 90
	right_analog_x = joystick.get_axis(3) * -90
	right_analog_y = joystick.get_axis(4) * 90

	time.sleep(.001)
	
	print("X:", left_analog_x, "Y:",left_analog_y)

	rightSpeed = 90 + (left_analog_y * -1) - left_analog_x
	leftSpeed = 90 + left_analog_y  - left_analog_x
	
	if rightSpeed < 0:
		rightSpeed = 0
	elif rightSpeed > 180:
		rightSpeed = 180

	if leftSpeed < 0:
		leftSpeed = 0
	elif leftSpeed > 180:
		leftSpeed = 180


	board.digital[BR].write(rightSpeed)
	board.digital[FR].write(rightSpeed)

	board.digital[BL].write(leftSpeed)
	board.digital[FL].write(leftSpeed)

	clock.tick(100)
quit()