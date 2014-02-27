#!/usr/bin/python
# Get current status from database:

import redis

R = redis.StrictRedis(host='localhost', port=6379, db=0)

print("Status: " + R.get('light:status'))
print("Nightmode: " + R.get('light:nightmode'))


