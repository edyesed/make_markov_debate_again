#!/usr/bin/env python
# make a discussion
import random
import time
import sys
from pymarkovchain import MarkovChain

NAMES = ['CLINTON', 'TRUMP', 'HOLT']
mcs = dict()
for idx, name in enumerate(NAMES):
  mcs[name] = MarkovChain('/var/tmp/markov_db.{0}'.format(name))

if __name__ == "__main__":
  while True:
    try:
      name = random.choice(NAMES)
      print(name +" : "+ unicode(mcs[name].generateString(), 'utf-8'))
      time.sleep(2)
    except KeyboardInterrupt:
      sys.exit()
