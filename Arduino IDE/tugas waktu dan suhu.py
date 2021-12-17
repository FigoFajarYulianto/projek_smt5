import pyfirmata
import time,datetime
board=pyfirmata.Arduino('COM4')
it=pyfirmata.util.Iterator(board)
it.start()
analog_input=board.get_pin('a:0:i')
while True:
  waktu=datetime.datetime.now()
  print("suhu ruangan pada :")
  print('%d:%d:%d'%(waktu.hour,waktu.minute,waktu.second))
  time.sleep(5)
  nilai_analog=analog_input.read()
  if nilai_analog is not None:
    waktu=time.time()
    suhu=5.0*100*nilai_analog
    print('adalah', suhu, 'celcius')
    time.sleep(5)
  
