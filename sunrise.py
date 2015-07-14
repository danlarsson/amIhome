import ephem
# Time in UTC!!
#

# Required libs:
# apt-get import python-dev
# apt-get import python-pip
# pip install pyaphem

earth = ephem.Observer()
earth.pressure = 0
earth.horizon = '-0:34'
earth.date = ephem.now()

# Returns a ephem time object of the time the sun rises
def sunrise(lat, long):
   earth.lat, earth.lon = lat, long
   return earth.previous_rising(ephem.Sun())

# Returns a ephem time object of the time the sun sets
def sunset(lat, long):
   earth.lat, earth.lon = lat, long
   return earth.next_setting(ephem.Sun())

# Returns a boolean, True if the sun is up now()
def daylight(lat, long):
   rise = sunrise(lat,long).real
   set = sunset(lat,long).real
   now = ephem.now().real

   if (now >= rise) and (now <= set) and (rise < set):
      return True
   else:
      return False

# Just some examples
def main():
   lat = '60.6754'
   long = '17.1509'
   print 'lat: ' + lat + ' | long: ' + long
   print 'Sunrise: ' + str(sunrise(lat,long)) + ' / ' + str(sunrise(lat,long).real)
   print 'Sunset: ' + str(sunset(lat,long)) + ' / ' + str(sunset(lat,long).real)
   print 'Now: ' + str(ephem.now()) + ' / ' + str(ephem.now().real)
   print 'Sun is up: ' + str(daylight(lat,long))


if __name__ == '__main__':
   main()
