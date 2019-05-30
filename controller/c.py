from pygame import *
clock = time.Clock()
import pygame, serial, time

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

	left_analog_x = joystick.get_axis(0)
	left_analog_y = joystick.get_axis(1)
	right_analog_x = joystick.get_axis(3)
	right_analog_y = joystick.get_axis(4)

	# if trying to get input from serial:
		# if arduinoData.inWaiting()

	if not waited: # this is going to wait for initialization
		time.sleep(1)
		waited = True
	
	if arduinoData.inWaiting(): # reads in the input from arduino
		print("ARDUINO:", str(arduinoData.readline())[2], "PYTHON:", left_analog_y)
		# print()
	else: # writes to the arduino
		arduinoData.write(str.encode(str(round(left_analog_y, 2))))
	# print(left_analog_y)


	clock.tick(20)

quit()