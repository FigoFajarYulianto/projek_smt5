import pyfirmata
import time

board = pyfirmata.Arduino('COM3')

while True:
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write
    time.sleep(1)