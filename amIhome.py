#!/usr/bin/python
import os, time, redis
import sunrise

# Logik!
# - If my phone is connected to the local network, turn on lights 
#	IF:
#	  It's dark outside
#	  The lights are off
#	  It's not sleep time. Don't want the lights to turn on when i sleep. Doh!       


phone_ip = "192.168.1.32"
lat = '60.6754'
long = '17.1509'
debug = 1 

def main():
    # Use Redis Database!
    R = redis.StrictRedis(host='localhost', port=6379, db=0)
    R.setnx('light:status', 0)  # If not exist set status to 0 = lights off
    R.setnx('light:nightmode', 0) # If not exist set nightmode to 0. 1 = do not turn on light.

    while 1:
	status = int(R.get('light:status')) # Read current light status

	if int(R.get('light:nightmode')) == 0: # If in nightmode, do noting.
           r = do_ping(phone_ip)  # Is the phone online
	
 	   if debug: # Debug
	      print(tid() + " Phone: " + str(r) + " Status: " + str(status)) + ' Daylight: ' + str(sunrise.daylight(lat, long))

	   # If the last status is off and the phone is reacheble, turn liggts on.
	   if (r == 1) and (status == 0) and not sunrise.daylight(lat, long):
 	      lights_on(1)
	      R.set('light:status', 1)
	   elif (r == 0) and (status == 1):
	      lights_off(1)
	      R.set('light:status', 0)

	rest(status) # Sleep a while


# If the phone was last in range, sleep 60 sec before next ping.
def rest(status):
   if status == 1:
      time.sleep(60)
   else:
      time.sleep(2)

# Turn lighs on with the use of telldus tool. id is the id of the light in telldus config.
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
#	( v )
#	 \|/ 
#
# Last line, it gets no better than this.
