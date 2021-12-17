from pyfirmata import util, Arduino
import time

#tentukan port arduino dengan komputer
board = Arduino('COM3')

#literasi pin arduino
it = util.Iterator(board)
it.start()

#baca nilai analog, disini terbaca sebagai float
nilai_analog = board.get_pin('a:0:i')

#void loop