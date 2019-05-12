from pyfirmata import Arduino, util
import time
board = Arduino("/dev/ttyACM1")
board.digital[3].write(1)
