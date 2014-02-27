import ephem

earth = ephem.Observer()
earth.pressure = 0
earth.horizon = '-0:34'
earth.date = ephem.now()


#print ephem.now()
#exit()

def sunrise(lat, long):
   earth.lat, earth.lon = lat, long
   return earth.previous_rising(ephem.Sun())

def sunset(lat, long):
   earth.lat, earth.lon = lat, long
   return earth.next_setting(ephem.Sun())

def daylight(lat, long):
   rise = sunrise(lat,long)
   set = sunset(lat,long)
   now = ephem.now()
   (z, z, z, hr, mr, z) =  rise.tuple()
   (z, z, z, hs, ms, z) =  set.tuple()
   (z, z, z, hn, mn, z) =  now.tuple()
#   if ((hn >= hr) and (mn >= mr)) and (hn

   print hr,mr
   print hs,ms
   print hn,mn
   exit()


def main():
   lat = '60.6754'
   long = '17.1509'
   print 'Sunrise: ' + str(sunrise(lat,long))
   print 'Sunset: ' + str(sunset(lat,long))
   print 'Sun is up' + daylight(lat,long)	



if __name__ == '__main__':
   main()
