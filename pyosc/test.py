#!/user/bin/python

import keyboard, OSC, time, os
from IPAddress import QLabIP, Lxip

send_address_SND = QLabIP, 53000
send_address = "192.168.1.100", 9000

c = OSC.OSCClient()
c.connect(send_address)

msg = OSC.OSCMessage()
msg1 = OSC.OSCMessage()
msg2 = OSC.OSCMessage()
msg3 = OSC.OSCMessage()
msg4 = OSC.OSCMessage()
msg5 = OSC.OSCMessage()
msg6 = OSC.OSCMessage()
clear_LX_cmd = OSC.OSCMessage()
sneak =  OSC.OSCMessage()

msg1.setAddress("/eos/key/go_to_cue")
msg2.setAddress("/eos/key/1")
msg3.setAddress("/eos/key/enter")

print(msg1)
c.send(msg1)
time.sleep(0.300)
c.send(msg2)
time.sleep(0.300)
c.send(msg3)
