import pyfirmata
import time
board=pyfirmata.Arduino('COM4')
it=pyfirmata.util.Iterator(board)
it.start()
analog_input=board.get_pin('a:0:i')
while True:
  nilai_analog=analog_input.read()
  if nilai_analog is not None:
    waktu=time.time()
    suhu=5.0*100*nilai_analog
    print(suhu,'celcius')
    time.sleep(1)

	    
