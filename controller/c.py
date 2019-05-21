from pygame import *
import pygame

screen = display.set_mode([500, 700])

init()
joystick.init()

clock = time.Clock()

running = True
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

	clock.tick(20)

quit()