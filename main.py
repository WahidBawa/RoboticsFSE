from pyfirmata import Arduino, util
import time
board = Arduino("/dev/ttyUSB00")
board.digital[13].write(1)