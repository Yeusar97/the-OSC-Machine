#!/user/bin/python

import keyboard, OSC, time, os
from IPAddress import QLabIP, Lxip

os.system("clear")

send_address_SND = QLabIP, 53000
send_address_LX = Lxip, 9000

c = OSC.OSCClient()
c.connect(send_address_SND)
c1 = OSC.OSCClient()
c1.connect(send_address_LX)

msg = OSC.OSCMessage()
msg1 = OSC.OSCMessage()
msg2 = OSC.OSCMessage()
msg3 = OSC.OSCMessage()
msg4 = OSC.OSCMessage()
msg5 = OSC.OSCMessage()
msg6 = OSC.OSCMessage()
clear_LX_cmd = OSC.OSCMessage()
sneak =  OSC.OSCMessage()

clear_LX_cmd.setAddress("/eos/key/clear_cmd")
sneak.setAddress("/eos/key/sneak")
def LED_COLOUR():
	print("Pick Colour")
	print("1: Red")
	print("2: Blue")
	print("3: Green")
	print("4: Purple")
	print("5: Aqua")
	print("6: Yellow")
	print("7: White")
	print("ESC: Return to All Options")
	time.sleep(1)
	print("Ready")
	c1.send(clear_LX_cmd)
	while True:
		if keyboard.is_pressed('esc'):
			break
		if keyboard.is_pressed('1'):
			msg2.setAddress("/eos/key/color_palette")
			msg3.setAddress("/eos/key/1")
			msg4.setAddress("/eos/key/enter")
			break
		if keyboard.is_pressed('2'):
			msg2.setAddress("/eos/key/color_palette")
			msg3.setAddress("/eos/key/2")
			msg4.setAddress("/eos/key/enter")
			break
		if keyboard.is_pressed('3'):
			msg2.setAddress("/eos/key/color_palette")
			msg3.setAddress("/eos/key/3")
			msg4.setAddress("/eos/key/enter")
			break
		if keyboard.is_pressed('4'):
			msg2.setAddress("/eos/key/color_palette")
			msg3.setAddress("/eos/key/4")
			msg4.setAddress("/eos/key/enter")
			break
		if keyboard.is_pressed('5'):
			msg2.setAddress("/eos/key/color_palette")
			msg3.setAddress("/eos/key/5")
			msg4.setAddress("/eos/key/enter")
			break
		if keyboard.is_pressed('6'):
			msg2.setAddress("/eos/key/color_palette")
			msg3.setAddress("/eos/key/6")
			msg4.setAddress("/eos/key/enter")
			break
		if keyboard.is_pressed('7'):
			msg2.setAddress("/eos/key/color_palette")
			msg3.setAddress("/eos/key/7")
			msg4.setAddress("/eos/key/enter")
			break

def RETURN_HOME():
	msg.setAddress('/eos/key/group')
	msg1.setAddress('/eos/key/9')
	msg2.setAddress('/eos/key/focus_palette')
	msg3.setAddress('/eos/key/1')
	msg4.setAddress('/eos/key/5')
	msg5.setAddress('/eos/key/enter')
	c1.send(msg)
	time.sleep(0.300)
	c1.send(msg1)
	time.sleep(0.300)
	c1.send(msg2)
	time.sleep(0.300)
	c1.send(msg3)
	time.sleep(0.300)
	c1.send(msg4)
	time.sleep(0.300)
	c1.send(msg5)
	msg.setAddress('/eos/key/group')
	msg1.setAddress('/eos/key/9')
	msg2.setAddress('/eos/key/color_palette')
	msg3.setAddress('/eos/key/7')
	msg4.setAddress('/eos/key/enter')
	c1.send(msg)
	time.sleep(0.300)
	c1.send(msg1)
	time.sleep(0.300)
	c1.send(msg2)
	time.sleep(0.300)
	c1.send(msg3)
	time.sleep(0.300)
	c1.send(msg4)
	msg.setAddress('/eos/key/group')
	msg1.setAddress('/eos/key/8')
	msg2.setAddress('/eos/key/color_palette')
	msg3.setAddress('/eos/key/7')
	msg5.setAddress('/eos/key/enter')
	c1.send(msg)
	time.sleep(0.300)
	c1.send(msg1)
	time.sleep(0.300)
	c1.send(msg2)
	time.sleep(0.300)
	c1.send(msg3)
	time.sleep(0.300)
	c1.send(msg4)
	msg.setAddress("/eos/key/group")
	msg1.setAddress("/eos/key/8")
	msg2.setAddress("/eos/key/@")
	msg3.setAddress("/eos/key/0")
	msg4.setAddress("/eos/key/enter")
	c1.send(msg)
	time.sleep(0.300)
	c1.send(msg1)
	time.sleep(0.300)
	c1.send(msg2)
	time.sleep(0.300)
	c1.send(msg3)
	time.sleep(0.300)
	c1.send(msg4)
		
def PAR_ON():
	msg.setAddress("/eos/key/group")
	msg1.setAddress("/eos/key/8")
	msg2.setAddress("/eos/key/@")
	msg3.setAddress("/eos/key/full")
	msg4.setAddress("/eos/key/enter")
	c1.send(msg)
	time.sleep(0.300)
	c1.send(msg1)
	time.sleep(0.300)
	c1.send(msg2)
	time.sleep(0.300)
	c1.send(msg3)
	time.sleep(0.300)
	c1.send(msg4)

def LED_POSITION():
	print("Focus Light to Someone's Exhibition")
	print("F1: Persia")
	print("F2: Rajiv")
	print("F3: Kensington")
	print("F4: Sarah")
	print("F5: Tarryn")
	print("F6: Isaac")
	print("F7: Ashleigh")
	print("F8: Michelle")
	print("F9: Jack")
	print("F10: Lina")
	print("F11: Kelly")
	print("F12: Katherine")
	print("F13: Sam")
	print("F14: Meika")
	print("esc: Return Home")
	c1.send(clear_LX_cmd) 
	while True:
		if keyboard.is_pressed("F1"):
			msg2.setAddress("/eos/key/focus_palette")
			msg3.setAddress("/eos/key/1")
			msg4.setAddress("/eos/key/enter")
			break
		if keyboard.is_pressed("F2"):
			msg2.setAddress("/eos/key/focus_palette")
			msg3.setAddress("/eos/key/2")
			msg4.setAddress("/eos/key/enter")
			break
		if keyboard.is_pressed("F3"):
			msg2.setAddress("/eos/key/focus_palette")
			msg3.setAddress("/eos/key/3")
			msg4.setAddress("/eos/key/enter")
			break
		if keyboard.is_pressed("F4"):
			msg2.setAddress("/eos/key/focus_palette")
			msg3.setAddress("/eos/key/4")
			msg4.setAddress("/eos/key/enter")
			break
		if keyboard.is_pressed("F5"):
			msg2.setAddress("/eos/key/focus_palette")
			msg3.setAddress("/eos/key/5")
			msg4.setAddress("/eos/key/enter")
			break
		if keyboard.is_pressed("F6"):
			msg2.setAddress("/eos/key/focus_palette")
			msg3.setAddress("/eos/key/6")
			msg4.setAddress("/eos/key/enter")
			break
		if keyboard.is_pressed("F7"):
			msg2.setAddress("/eos/key/focus_palette")
			msg3.setAddress("/eos/key/7")
			msg4.setAddress("/eos/key/enter")
			break
		if keyboard.is_pressed("F8"):
			msg2.setAddress("/eos/key/focus_palette")
			msg3.setAddress("/eos/key/8")
			msg4.setAddress("/eos/key/enter")
			break
		if keyboard.is_pressed("F9"):
			msg2.setAddress("/eos/key/focus_palette")
			msg3.setAddress("/eos/key/9")
			msg4.setAddress("/eos/key/enter")
			break
		if keyboard.is_pressed("F10"):
			msg2.setAddress("/eos/key/focus_palette")
			msg3.setAddress("/eos/key/1")
			msg5.setAddress("/eos/key/0")
			msg4.setAddress("/eos/key/enter")
			break
		if keyboard.is_pressed("F11"):
			msg2.setAddress("/eos/key/focus_palette")
			msg3.setAddress("/eos/key/1")
			msg5.setAddress("/eos/key/1")
			msg4.setAddress("/eos/key/enter")
			break
		if keyboard.is_pressed("F12"):
			msg2.setAddress("/eos/key/focus_palette")
			msg3.setAddress("/eos/key/1")
			msg5.setAddress("/eos/key/2")
			msg4.setAddress("/eos/key/enter")
			break
		if keyboard.is_pressed("F13"):
			msg2.setAddress("/eos/key/focus_palette")
			msg3.setAddress("/eos/key/1")
			msg5.setAddress("/eos/key/3")
			msg4.setAddress("/eos/key/enter")
			break
		if keyboard.is_pressed("F14"):
			msg2.setAddress("/eos/key/focus_palette")
			msg3.setAddress("/eos/key/1")
			msg5.setAddress("/eos/key/4")
			msg4.setAddress("/eos/key/enter")
			break
		if keyboard.is_pressed("esc"):
			msg2.setAddress("/eos/key/focus_palette")
			msg3.setAddress("/eos/key/1")
			msg5.setAddress("/eos/key/5")
			msg4.setAddress("/eos/key/enter")
			break

def WHAT_DO():
	print("Hi! Welcome to my exhibition, the OSC Machine")
	time.sleep(0.500)
	print("OSC is a fabulous protocol which allows a lot to happen with some basic coding knowledge")
	time.sleep(0.500)
	print("Please look below for pre-coded options that are ready to go!")
	time.sleep(0.500)
	print("Press 1 to see additional instructions for chances to change LX")
	time.sleep(0.500)
	print("Press Q, W, E, R, or T to listen to my SND Design")
	time.sleep(0.500)
	print("Press A to listen to an iconic sound of Technical Production in our theatres")
	time.sleep(0.500)
	print("Press Z, X, or C to watch some VIS Design I have created")
	time.sleep(0.500)
	print("Press V to watch a short video featuring my LX Design on Twelfth Night, a QUT Production")
	time.sleep(0.500)
	print("Press S if you want to stop listening to my SND Design")
	time.sleep(0.500)
	print("Press D if you want to stop watching my VIS Design or my LX Design video")
	time.sleep(0.500)
	print("Press H if you want to find out more about me")
	time.sleep(0.500)
	print("press U to hear Michelle's Exhibition Sound")
	time.sleep(0.500)
	print("press I to hear Kelly's Exhibition Sound")
	time.sleep(0.500)
	print("Press O to hear Tarryn's Exhibition Sound")
	time.sleep(0.500)
	print("Press P to hear Ashleigh's Exhibition Sound")
	time.sleep(0.500)
	print("The exhibition soundscapes will be unlocked after the curated experiece")
	time.sleep(0.500)
	print("Once the word Ready appears, the OSC Machine is ready to receive your command")
	time.sleep(0.500)

while True:
	if keyboard.is_pressed("i"):
		print("Listen in to Kelly's Sound - to experience it, walk over to her exhibition")
		msg.setAddress("/cue/EXH1/start")
		print("Standby")
		c.send(msg)
		time.sleep(1)
		print("Ready")
	if keyboard.is_pressed("o"):
		print("Listen in to Tarryn's Sound - to experience it, walk over to her exhibition")
		msg.setAddress("/cue/EXH2/start")
		c.send(msg)
		time.sleep(1)
		print("Ready")
	if keyboard.is_pressed("u"):
		print("Listen in to Michelle's Sound - to experience it, walk over to her exhibition")
		msg.setAddress("/cue/EXH4/start")
		c.send(msg)
		time.sleep(1)
		print("Ready")
	if keyboard.is_pressed("p"):
		print("Listen in to Ashleigh's Sound - to experience it, walk over to there exhibition")
		msg.setAddress("/cue/EXH3/start")
		c.send(msg)
		time.sleep(1)
		print("Ready")
	if keyboard.is_pressed(" "):
		WHAT_DO()
		time.sleep(3)
		print("Press a key and have fun!")
		time.sleep(1)
		print("Ready!")
	if keyboard.is_pressed('q'):
		msg.setAddress("/cue/ZAC(1)/start")
		print("Play Virtual Production: Speaking in Tongues Opening Sound Design")
		print("Standby")
		c.send(msg)
		time.sleep(5)
		print("Ready")
 	if keyboard.is_pressed('w'):
		msg.setAddress("/cue/ZAC(2)/start")
		print("Play Mama's Boys Collective: Ocean Sequence Sound Design")
		print("Standby")
		c.send(msg)
		time.sleep(5)
		print("Ready")
	if keyboard.is_pressed('e'):
		msg.setAddress("/cue/ZAC(3)/start")
		print("Play Mama's Boys Collective: Police Arrive Sound Design")
		print("Standby")
		c.send(msg)
		time.sleep(5)
		print("Ready")
	if keyboard.is_pressed('a'):
		msg.setAddress("/cue/Atmos/start")
		print("Listen in for the fun sound effect")
		print("Standby")
		c.send(msg)
		time.sleep(5)
		print("Ready")
	if keyboard.is_pressed('v'):
		msg.setAddress("/cue/ZAC(LX)/start")
		print("Play Twelfth Night: A video of my LX Design")
		print("Standby")
		c.send(msg)
		time.sleep(5)
		print("Ready")
	if keyboard.is_pressed('r'):
		msg.setAddress("/cue/ZAC(4)/start")
		print("Play Virtual Productions: Speaking in Tongues Emotive Piano Section")
		print("Standby")
		c.send(msg)
		time.sleep(5)
		print("Ready")
	if keyboard.is_pressed('t'):
		msg.setAddress("/cue/ZAC(5)/start")
		print("Play Virtual Productions: Speaking in Tongues Dream to Nightmare Atmosphere")
		c.send(msg)
		time.sleep(5)
		print("Ready")
	if keyboard.is_pressed('s'):
		msg.setAddress("/cue/ZAC(SNDSTOP)/start")
		print("Stopping all Tracks")
		print("Standby")
		c.send(msg)
		time.sleep(3)
		print("Ready")
	if keyboard.is_pressed('d'):
		msg.setAddress("/cue/ZAC(VISSTOP)/start")
		print("Stopping Vision Content")
		print("Standby")
		c.send(msg)
		time.sleep(3)
		print("Ready")
	if keyboard.is_pressed('z'):
		msg.setAddress("/cue/ZAC(6)/start")
		print("Playing Twelfth Night Vision Content")
		time.sleep(0.500)
		print("Please note the surface for this show was a LED Wall 12 panels long by 2 wide")
		time.sleep(0.500)
		print("The content here has been resized to fit nicer on the monitor")
		time.sleep(0.500)
		c.send(msg)
		print("Standby")
		time.sleep(3)
		print("Ready")
	if keyboard.is_pressed('x'):
		msg.setAddress("/cue/ZAC(7)/start")
		print("Playing Production Arts Project: Panopticon Surveillance to Profiling Section")
		print("Standby")
		c.send(msg)
		time.sleep(3)
		print("Ready")
	if keyboard.is_pressed('c'):
		msg.setAddress("/cue/ZAC(8)/start")
		print("Playing Production Arts Project: Panopticon Preshow Vision Content")
		c.send(msg)
		time.sleep(3)
		print("Ready")
	if keyboard.is_pressed('h'):
		msg.setAddress("/cue/ZAC(WAI)/start")
		print("You want to know who I am, here is a short video exploring who I am")
		print("Standby")
		c.send(msg)
		time.sleep(3)
		print("Ready")
	if keyboard.is_pressed('1'):
		print("Select Fixture")
		print("1: Zachary's Moving Light")
		print("2: Zachary's LED Pars")
		print("ESC: Return to All Options")
		time.sleep(1)
		print("Ready")
		while True:
			if keyboard.is_pressed('esc'):
				break
			if keyboard.is_pressed('2'):
				PAR_ON()
				time.sleep(0.300)
				msg.setAddress("/eos/key/group")
				msg1.setAddress("/eos/key/8")
				time.sleep(0.300)
				LED_COLOUR()
				c1.send(msg)
				time.sleep(0.300)
				c1.send(msg1)
				time.sleep(0.300)
				c1.send(msg2)
				time.sleep(0.300)
				c1.send(msg3)
				time.sleep(0.300)
				c1.send(sneak)
				time.sleep(0.300)
				c1.send(msg4)
				time.sleep(5)
				print("Standby")
				RETURN_HOME()
				time.sleep(3)
				print("Ready")
				break
			if keyboard.is_pressed('1'):
				msg.setAddress("/eos/key/group")
				msg1.setAddress("/eos/key/9")
				print(msg)
				print("1: Colour")
				print("2: Position")
				time.sleep(1)
				print("Ready")
				while True:
					if keyboard.is_pressed("1"):
						LED_COLOUR()
						break
					if keyboard.is_pressed('2'):
						LED_POSITION()
						break
				c1.send(msg)
				time.sleep(0.300)
				c1.send(msg1)
				time.sleep(0.300)
				c1.send(msg2)
				time.sleep(0.300)
				c1.send(msg3)
				time.sleep(0.300)
				c1.send(msg5)
				time.sleep(0.300)
				c1.send(msg4)
				print("Standby")
				time.sleep(5)
				RETURN_HOME()
				time.sleep(3)
				print("Ready")
				break
