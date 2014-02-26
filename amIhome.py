#!/usr/bin/python

import os, time

# Logik!
# 1. om telefonen svara pa ping, tand lampa
#       om det ar morkt ute.
#       om lamporna inte redan ar pa (spelar ingen roll)
#	om sleepmode, strombrytare vid sangen, tand inte lampor pa ett dygn.
#       

phone_ip = "192.168.1.32"
debug = 1 

def main():
    status = 0  # Current light status

    while 1:
        r = do_ping(phone_ip)  # Is the phone online

	if debug: # Debug
	   print(tid() + " Phone: " + str(r) + " Status: " + str(status))

	# If the last status is off and the phone is reacheble, turn liggts on.
	if (r == 1) and (status == 0):
 	   lights_on(3)
	   status = 1
	elif (r == 0) and (status == 1):
	   lights_off(3)
	   status = 0

	# If the phone was last in range, sleep 60 sec before next ping.
	if status == 1:
	   time.sleep(60)
	else:
	   time.sleep(2)

# Turn lighs on with the use of telldus tool
def lights_on(id):
  os.system("/usr/bin/tdtool --on " + str(id))

# Turn the lights off with the telldus tool
def lights_off(id):
  os.system("/usr/bin/tdtool --off " + str(id))

# Well.. Ping!
def do_ping(ip):
  response = os.system("ping -c 1 " + ip + " > /dev/null 2>&1")
  if response == 0:
    return 1
  else:
    return 0

# Returns time, use for Debug
def tid():
   tm = time.localtime()
   tid = str(tm[3]) + ":" + str(tm[4]) + ":" + str(tm[5])
   return(tid)



# Strange and stupid Python code.
if __name__ == '__main__':
    main()


#	(. .) 
#	 ).(
#	/ v \
#	\ | / 
#
# Last line, it gets no better than this.
