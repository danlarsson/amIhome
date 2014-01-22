#!/usr/bin/python

import os, time

# Logik!
# 

def main():
    while 1:
        r = do_ping('192.168.1.32')
	print(r)
	time.sleep(2)



def do_ping(ip):
  response = os.system("ping -c 1 " + ip + " > /dev/null 2>&1")

  if response == 0:
    return 1
  else:
    return 0



if __name__ == '__main__':
    main()
