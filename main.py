from pygame import *
clock = time.Clock()
import pygame, serial, time

import os

os.environ["SDL_VIDEODRIVER"] = "dummy"

###################################################################### this is all firmata stuff
import pyfirmata
from pyfirmata import Arduino, util
board = Arduino("/dev/ttyACM0")

iterator = util.Iterator(board)
iterator.start();
 
FL = 4
BL = 3
FR = 6
BR = 5
  
leftSuck = 8
rightSuck = 7

ballLift = 9

motor = 10

elevator = 13

right_qtr = 0
left_qtr = 1

board.digital[FL].mode = pyfirmata.SERVO
board.digital[BL].mode = pyfirmata.SERVO
board.digital[FR].mode = pyfirmata.SERVO
board.digital[BR].mode = pyfirmata.SERVO

board.digital[leftSuck].mode = pyfirmata.SERVO
board.digital[rightSuck].mode = pyfirmata.SERVO

board.digital[ballLift].mode = pyfirmata.SERVO

board.digital[elevator].mode = pyfirmata.SERVO

board.digital[motor].mode = pyfirmata.DIGITAL

#board.analog[right_qtr].mode = pyfirmata.ANALOG
#board.analog[left_qtr].mode = pyfirmata.ANALOG

board.analog[right_qtr].enable_reporting()
board.analog[left_qtr].enable_reporting()
#board.analog[right_qtr].enable_reporting()
#boar

board.digital[FL].write(90)
board.digital[BL].write(90)
board.digital[FR].write(90)
board.digital[BR].write(90)

board.digital[leftSuck].write(90)
board.digital[rightSuck].write(90)

board.digital[ballLift].write(180)

board.digital[elevator].write(88)
######################################################################
screen = display.set_mode([500, 700])

init()
joystick.init()

joystickConnected = False

running = True
while running:
	for evt in event.get():
		if evt.type == QUIT:
			running = False
	if (not joystickConnected):
		try:
			pygame.joystick.quit()
			pygame.joystick.init()
			joystick = pygame.joystick.Joystick(0)
			joystick.init()
			joystickConnected = True
		except:
			print("waiting to connect ...")

	else:
#		board.iterate()

		cross_button = joystick.get_button(0)
		circle_button = joystick.get_button(1)
		triangle_button = joystick.get_button(2)
		square_button = joystick.get_button(3)

		L1 = joystick.get_button(4)
		R1 = joystick.get_button(5)

		left_analog_x = joystick.get_axis(0) * -90
		left_analog_y = joystick.get_axis(1) * 90
		right_analog_x = joystick.get_axis(2) * -90
		right_analog_y = joystick.get_axis(5) * 90

		L2 = round(joystick.get_axis(3), 2)
		R2 = round(joystick.get_axis(4), 2)

		right_qtr_val = board.analog[right_qtr].read() * 1000
		left_qtr_val = board.analog[left_qtr].read() * 1000

		time.sleep(.001)
		
#		print("LX:", round(left_analog_x, 2), "LY:", round(left_analog_y, 2), "RX:", round(right_analog_x, 2), "RY:", round(right_analog_y, 2))
#		print("L1:", L1, "R1:", R1)
#		print("L2:", L2, "R2:", R2, "\n")
		
		print("R_QTR:", right_qtr_val, "L_QTR:", left_qtr_val)

		rightSpeed = 90 + (left_analog_y) - left_analog_x
		leftSpeed = 90 + (left_analog_y * -1)  - left_analog_x

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

		board.digital[leftSuck].write(90 + right_analog_y)
		board.digital[rightSuck].write(90 + right_analog_y * -1)

		if L1 == 1:
			board.digital[ballLift].write(180)
		elif R1 == 1:
			board.digital[ballLift].write(0)
		
		if R2 == 1:
			board.digital[elevator].write(180)
		elif L2 == 1:
			board.digital[elevator].write(0)
		else:
			board.digital[elevator].write(90)
		

		if (cross_button):
			if (board.analog[left_qtr].read() < 800):
				board.digital[BR].write(180)
				board.digital[FR].write(180)
				
				board.digital[BL].write(0)
				board.digital[FL].write(0)

			if (board.analog[right_qtr].read() < 800):
				board.digital[BR].write(0)
				board.digital[FR].write(0)

				board.digital[BL].write(180)
				board.digital[FL].write(180)				
	clock.tick(60)
quit()
