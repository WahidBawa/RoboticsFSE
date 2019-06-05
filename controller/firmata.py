import pyfirmata
from pyfirmata import Arduino, util
import time
waited = False
board = Arduino("/dev/ttyACM0")


iterator = util.Iterator(board)
iterator.start();


val = board.get_pin("a:0:i")
while True:
	# if not waited:
	# 	time.sleep(1)
	# 	waited = True;
	time.sleep(.01)
	print(val.read())

board.exit() 