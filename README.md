# the-OSC-Machine
Zachary Neville's Standing By 2020 Raspberry Pi Code

The code here is a little rough but fully functioning for the technical production showcase at QUT

The reason I have uploaded it to here is to give anyone who want to take a look into how I have coded my Raspberry Pi to interact with the control systems of our exhibition

to break it down the librarys installed are:
  -pyosc
  -keyboard
  -os
  -time

All of the scripts are coded in python, and certain OSC scripts are inserted to send when required. 

Files of interest:
  -IPAddress.py (change the IP addresses of the control systems you are looking to control)
  -myOSC.py (the meat and potatoes of the project. Everything of interest occurs in here, open it up and take a look at how I coded it).
  
I will continue on this project to ultimately showcase how useful the OSC protocol can be, and show how fun controlling all facets of a theatre can be.
