Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pyfirmata

pin=6
board=pyfirmata.Arduino('/dev/ttyACM0')

while True:
board.digital[pin].write(1)
board.pass_time(1)
board.digital[pin].write(0)
board.pass_time(1)
SyntaxError: multiple statements found while compiling a single statement
>>> import pyfirmata
>>> pin=6
>>> board=pyfirmata.Arduino('COM4')
w
>>> while True:
	board.digital[pin].write(1)
	board.pass_time(1)
	board.digital[pin].write(0)
	board.pass_time(1)

	

================================ RESTART: Shell ================================
>>> import pyfirmata
>>> pin=6
>>> pinA=7
>>> pinB=8
>>> pinC=9
>>> 
================================ RESTART: Shell ================================
>>> import pyfirmata
>>> from time import sleep
>>> pin=5
>>> board=pyfirmata.Arduino('COM4')
>>> while True:
	board.digital[pin].write(1)
	sleep(1)
	board.digital[pin].write(0)
	sleep(1)

	

================================ RESTART: Shell ================================
>>> import pyfirmata
>>> import time
>>> board=pyfirmata.Arduino('COM4')
>>> it=pyfirmata.util.Iterator(board)
>>> it.start()
>>> analog_input=board.get_pin('a:0:i')
>>> while True:
	nilai_analog=analog_input.read()
	print(nilai_analog)
	time.sleep(0.2)

	
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1251
0.1261
0.1251
0.1261
0.1251
0.1251
0.1251
0.1251
0.1251
0.1271
0.1251
0.1251
0.1251
0.1232
0.1261
0.1251
0.349
0.7361
0.7351
0.7361
0.737
0.7449
0.8866
0.9286
0.9492
0.9492
0.9844
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
1.0
0.9462
0.8309
0.7928
0.65
0.6393
0.6413
0.5748
0.4585
0.347
0.3255
0.3255
0.3255
0.3265
0.3294
0.3265
0.3275
0.3656
0.3656
0.3627
0.3646
0.2023
0.0528
0.4272
0.0
0.0
0.1134
0.1173
0.3284
0.4272
0.4262
0.3558
0.2151
0.1202
0.1202
0.2737
0.48
0.5054
0.4418
0.1984
0.1906
0.1906
0.2307
0.3715
0.4057
0.4057
0.4037
0.4076
0.6471
0.7683
0.7693
0.7683
0.7234
0.6149
0.4565
0.2678
0.2688
0.4673
0.4888
0.3392
0.2239
0.2239
0.5582
0.8592
0.8631
0.6031
0.3754
0.2825
0.5288
0.9883
1.0
0.8446
0.607
0.5787
0.5787
0.5787
0.5503
0.5484
0.5503
0.5494
0.5425
0.5406
0.5718
0.6041
0.7331
0.8504
1.0
1.0
1.0
1.0
0.7918
0.694
0.6931
0.9189
1.0
1.0
0.8739
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.782
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781
0.781

================================ RESTART: Shell ================================
>>> import pyfirmata
>>> import time
>>> board=pyfirmata.Arduino('COM4')
>>> it=pyfirmata.util.Iterator(board)
>>> it.start()
>>> analog_input=board.get_pin('a:0:i')
>>> while True:
	nilai_analog=analog_input.read()
	if nilai_analog is not None:
		waktu=date
		suhu=5.0*100*nilai_analog
		print(suhu,'celcius')
		time.sleep(1)

		
Traceback (most recent call last):
  File "<pyshell#50>", line 4, in <module>
    waktu=date
NameError: name 'date' is not defined
>>> time
<module 'time' (built-in)>
>>> date
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    date
NameError: name 'date' is not defined
>>> waktu
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    waktu
NameError: name 'waktu' is not defined
>>> sensor suhu
SyntaxError: invalid syntax
>>> sensor suhu.py
SyntaxError: invalid syntax
>>> 
=============== RESTART: C:/Users/LENOVO/Documents/sensor suhu.py ==============
Traceback (most recent call last):
  File "C:/Users/LENOVO/Documents/sensor suhu.py", line 10, in <module>
    waktu=datetime.now()
NameError: name 'datetime' is not defined
>>> import time
>>> waktu=time.time()
>>> print(waktu)
1637548992.138108
>>> 
=============== RESTART: C:/Users/LENOVO/Documents/sensor suhu.py ==============
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
392.0 celcius
391.0 celcius
391.0 celcius
390.5 celcius
391.0 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
391.0 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius
390.5 celcius

================================ RESTART: Shell ================================
>>> 
============= RESTART: C:/Users/LENOVO/Documents/manampilkan jam.py ============
9:49:26
9:49:27
9:49:28
9:49:29
9:49:30
9:49:31
9:49:32
9:49:33
9:49:35
9:49:36
9:49:37
9:49:38
9:49:39

================================ RESTART: Shell ================================
>>> 
========== RESTART: C:/Users/LENOVO/Documents/tugas waktu dan suhu.py ==========
9:50:49
390.5 celcius
9:50:51
390.5 celcius
9:50:53
390.5 celcius
9:50:55
390.5 celcius
9:50:57

================================ RESTART: Shell ================================
>>> 
========== RESTART: C:/Users/LENOVO/Documents/tugas waktu dan suhu.py ==========
9:58:15
9:58:16
9:58:17
9:58:18
9:58:19
9:58:20
9:58:21
9:58:22

================================ RESTART: Shell ================================
>>> 
========== RESTART: C:/Users/LENOVO/Documents/tugas waktu dan suhu.py ==========
Traceback (most recent call last):
  File "C:/Users/LENOVO/Documents/tugas waktu dan suhu.py", line 9, in <module>
    print('%d:%d:%d'%('suhu ruangan pada',waktu.hour,waktu.minute,waktu.second,'adalah'))
TypeError: %d format: a number is required, not str
>>> 
========== RESTART: C:\Users\LENOVO\Documents\tugas waktu dan suhu.py ==========
Traceback (most recent call last):
  File "C:\Users\LENOVO\Documents\tugas waktu dan suhu.py", line 9, in <module>
    print('%d:%d:%d'%('suhu ruangan pada',waktu.hour,waktu.minute,waktu.second,'adalah'))
TypeError: %d format: a number is required, not str
>>> 
========== RESTART: C:\Users\LENOVO\Documents\tugas waktu dan suhu.py ==========
Traceback (most recent call last):
  File "C:\Users\LENOVO\Documents\tugas waktu dan suhu.py", line 9, in <module>
    print('%d:%d:%d'%("suhu ruangan pada",waktu.hour,waktu.minute,waktu.second,"adalah"))
TypeError: %d format: a number is required, not str
>>> 
========== RESTART: C:\Users\LENOVO\Documents\tugas waktu dan suhu.py ==========
10:2:6
390.5 celcius
10:2:16
390.5 celcius
10:2:26
390.5 celcius
10:2:36
391.0 celcius
10:2:46
390.5 celcius
10:2:56
390.5 celcius
10:3:6
390.5 celcius
10:3:16
390.5 celcius
10:3:26
391.0 celcius
10:3:36
390.5 celcius
10:3:47
390.5 celcius
10:3:57
390.5 celcius
10:4:7
390.5 celcius
10:4:17
390.5 celcius
10:4:27
390.5 celcius
10:4:37
390.5 celcius
10:4:47
390.5 celcius
10:4:57
390.5 celcius
10:5:7
390.5 celcius
10:5:17
390.5 celcius
10:5:27
390.5 celcius
10:5:37
390.5 celcius
10:5:48
390.5 celcius
10:5:58
390.5 celcius

========== RESTART: C:\Users\LENOVO\Documents\tugas waktu dan suhu.py ==========
10:6:13
waktu 1637550378.31934 suhu 390.5 celcius
10:6:23
waktu 1637550388.4272668 suhu 390.5 celcius
10:6:33
waktu 1637550398.517424 suhu 390.5 celcius

========== RESTART: C:\Users\LENOVO\Documents\tugas waktu dan suhu.py ==========
waktu 1637550412.7220716 suhu 390.5 celcius
waktu 1637550422.851384 suhu 390.5 celcius
waktu 1637550432.9078789 suhu 390.5 celcius
waktu 1637550443.0161395 suhu 390.5 celcius
waktu 1637550453.1316607 suhu 390.5 celcius
waktu 1637550463.2295926 suhu 390.5 celcius
waktu 1637550473.292234 suhu 390.5 celcius
waktu 1637550483.397648 suhu 390.5 celcius
waktu 1637550493.5043406 suhu 390.5 celcius
waktu 1637550503.5687716 suhu 390.5 celcius
waktu 1637550513.6211832 suhu 390.5 celcius
waktu 1637550523.6663487 suhu 390.5 celcius
waktu 1637550533.7158718 suhu 390.5 celcius
waktu 1637550543.7762146 suhu 390.5 celcius
waktu 1637550553.8425589 suhu 390.5 celcius
waktu 1637550563.8989868 suhu 390.5 celcius
waktu 1637550573.993503 suhu 390.5 celcius
waktu 1637550584.0688884 suhu 390.5 celcius
waktu 1637550594.132034 suhu 390.5 celcius
waktu 1637550604.2174177 suhu 390.5 celcius
waktu 1637550614.275176 suhu 390.5 celcius

========== RESTART: C:\Users\LENOVO\Documents\tugas waktu dan suhu.py ==========
Traceback (most recent call last):
  File "C:\Users\LENOVO\Documents\tugas waktu dan suhu.py", line 15, in <module>
    print('%d:%d:%d'%(waktu.hour,waktu.minute,waktu.second),'adalah',suhu,'celcius')
AttributeError: 'float' object has no attribute 'hour'
>>> 
========== RESTART: C:\Users\LENOVO\Documents\tugas waktu dan suhu.py ==========
Traceback (most recent call last):
  File "C:\Users\LENOVO\Documents\tugas waktu dan suhu.py", line 15, in <module>
    print(waktu.hour,waktu.minute,waktu.second,'suhu',suhu,'celcius')
AttributeError: 'float' object has no attribute 'hour'
>>> 
========== RESTART: C:\Users\LENOVO\Documents\tugas waktu dan suhu.py ==========
waktu 1637550826.9954393 suhu 391.0 celcius
waktu 1637550837.1229773 suhu 390.5 celcius
waktu 1637550847.222087 suhu 390.5 celcius
waktu 1637550857.306149 suhu 390.5 celcius
waktu 1637550867.3757823 suhu 390.5 celcius

========== RESTART: C:\Users\LENOVO\Documents\tugas waktu dan suhu.py ==========
suhu rungan pada 1637550887.1494482 adalah 390.5 celcius
suhu rungan pada 1637550897.2165344 adalah 390.5 celcius
suhu rungan pada 1637550907.2830765 adalah 390.5 celcius
suhu rungan pada 1637550917.3507304 adalah 390.5 celcius

========== RESTART: C:\Users\LENOVO\Documents\tugas waktu dan suhu.py ==========
Traceback (most recent call last):
  File "C:\Users\LENOVO\Documents\tugas waktu dan suhu.py", line 15, in <module>
    print('suhu rungan pada','%d:%d:%d'%(waktu.hour,waktu.minute,waktu.second),'adalah',suhu,'celcius')
AttributeError: 'float' object has no attribute 'hour'
>>> 
========== RESTART: C:\Users\LENOVO\Documents\tugas waktu dan suhu.py ==========
Traceback (most recent call last):
  File "C:\Users\LENOVO\Documents\tugas waktu dan suhu.py", line 15, in <module>
    print('suhu rungan pada',('%d:%d:%d'%(waktu.hour,waktu.minute,waktu.second)),'adalah',suhu,'celcius')
AttributeError: 'float' object has no attribute 'hour'
>>> 
========== RESTART: C:\Users\LENOVO\Documents\tugas waktu dan suhu.py ==========
Traceback (most recent call last):
  File "C:\Users\LENOVO\Documents\tugas waktu dan suhu.py", line 15, in <module>
    print('suhu rungan pada',('%d:%d:%d'%(waktu.hour,waktu.minute,waktu.second)), 'suhu', suhu, 'celcius')
AttributeError: 'float' object has no attribute 'hour'
>>> 
========== RESTART: C:\Users\LENOVO\Documents\tugas waktu dan suhu.py ==========
Traceback (most recent call last):
  File "C:\Users\LENOVO\Documents\tugas waktu dan suhu.py", line 15, in <module>
    print('suhu rungan pada %d:%d:%d'%(waktu.hour,waktu.minute,waktu.second), 'suhu', suhu, 'celcius')
AttributeError: 'float' object has no attribute 'hour'
>>> 
========== RESTART: C:\Users\LENOVO\Documents\tugas waktu dan suhu.py ==========
Traceback (most recent call last):
  File "C:\Users\LENOVO\Documents\tugas waktu dan suhu.py", line 15, in <module>
    print('%d:%d:%d'%(waktu.hour,waktu.minute,waktu.second), 'suhu', suhu, 'celcius')
AttributeError: 'float' object has no attribute 'hour'
>>> 
========== RESTART: C:\Users\LENOVO\Documents\tugas waktu dan suhu.py ==========
waktu :
10:21:27
suhu 390.5 celcius
waktu :
10:21:37
suhu 390.5 celcius
waktu :
10:21:47
suhu 390.5 celcius
waktu :
10:21:57
suhu 390.5 celcius
waktu :
10:22:7
suhu 390.5 celcius
waktu :
10:22:17
suhu 390.5 celcius
waktu :
10:22:27
suhu 390.5 celcius
waktu :
10:22:37
suhu 390.5 celcius

========== RESTART: C:\Users\LENOVO\Documents\tugas waktu dan suhu.py ==========
Traceback (most recent call last):
  File "C:\Users\LENOVO\Documents\tugas waktu dan suhu.py", line 16, in <module>
    print('%d:%d:%d'%(waktu.hour,waktu.minute,waktu.second))
AttributeError: 'float' object has no attribute 'hour'
>>> 
========== RESTART: C:\Users\LENOVO\Documents\tugas waktu dan suhu.py ==========
suhu ruangan pada :
10:24:32
adalah 390.5 celcius
suhu ruangan pada :
10:24:42
adalah 390.5 celcius
suhu ruangan pada :
10:24:52
adalah 390.5 celcius
suhu ruangan pada :
10:25:2
adalah 390.5 celcius
suhu ruangan pada :
10:25:13
adalah 390.5 celcius
suhu ruangan pada :
10:25:23
adalah 390.5 celcius
suhu ruangan pada :
10:25:33

================================ RESTART: Shell ================================
>>> 