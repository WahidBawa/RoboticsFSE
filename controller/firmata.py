import pyfirmata
from pyfirmata import Arduino, util
import time

board = Arduino("/dev/ttyACM0")

time.sleep(1)

iterator = util.Iterator(board)
iterator.start();

# x = board.get_pin("a:5:i")
# x.enable_reporting()
board.analog[0].mode = pyfirmata.INPUT
board.analog[0].enable_reporting()
print(board.analog[0].read())


# while True:
	# print(x.read())

board.exit() 