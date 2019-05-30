from pygame import *
clock = time.Clock()
import pygame, serial, time

###################################################################### this is all firmata stuff
import pyfirmata
from pyfirmata import Arduino, util
waited = False
board = Arduino("/dev/ttyACM0")


iterator = util.Iterator(board)
iterator.start();

val = board.get_pin("a:0:i")

FL = 6
BL = 5
FR = 4
BR = 3

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
waited = False;
arduinoData = serial.Serial("/dev/ttyACM1", 9600, timeout = 5)
while running:
	for evt in event.get():
		if evt.type == QUIT:
			running = False

		if evt.type == JOYBUTTONDOWN:
			print("Joystick button pressed.")
		if evt.type == JOYBUTTONUP:
			print("Joystick button released.")

	joystick = pygame.joystick.Joystick(0)
	joystick.init()

	cross_button = joystick.get_button(0)
	circle_button = joystick.get_button(1)
	triangle_button = joystick.get_button(2)
	square_button = joystick.get_button(3)

	left_analog_x = joystick.get_axis(0) * 90
	left_analog_y = joystick.get_axis(1) * 90
	right_analog_x = joystick.get_axis(3) * 90
	right_analog_y = joystick.get_axis(4) * 90

	time.sleep(.01)
	
	print(left_analog_y)

	board.digital[BR].write(90 + left_analog_y * -1)
	board.digital[FR].write(90 + left_analog_y * -1)

	board.digital[BL].write(90 + left_analog_y)
	board.digital[FL].write(90 + left_analog_y)

	clock.tick(100)

quit()