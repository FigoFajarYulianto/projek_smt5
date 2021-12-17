import pyfirmata
import time,datetime
board=pyfirmata.Arduino('COM4')
it=pyfirmata.util.Iterator(board)
it.start()
analog_input=board.get_pin('a:0:i')
while True:
  waktu=datetime.datetime.now()
  print('%d:%d:%d'%(waktu.hour,waktu.minute,waktu.second))
  time.sleep(1)
