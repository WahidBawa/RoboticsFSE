import pyfirmata
import time
board = pyfirmata.Arduino("/dev/ttyACM2")
it = pyfirmata.util.Iterator(board)
it.start()
pin9 = board.get_pin('d:9:p');
while True:
	pin9.write(90)

