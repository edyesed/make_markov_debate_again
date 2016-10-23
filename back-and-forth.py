#!/usr/bin/env python
# make a discussion
import requests
import random
import time
import sys
import json
import os
import glob
import re
from pymarkovchain import MarkovChain
from bisect import bisect

# From SO. This is a way to do it without numpy
# http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice/4322940#4322940
def weighted_choice(choices):
    values, weights = zip(*choices)
    total = 0
    cum_weights = []
    for w in weights:
        total += w
        cum_weights.append(total)
    x = random.random() * total
    i = bisect(cum_weights, x)
    return values[i]

if __name__ == "__main__":
  files = glob.glob("/var/tmp/markov_db.*")
  mcs = dict()
  for file in files:
    # this matches the all caps bits at the end of the file name
    m = re.search("/var/tmp/markov_db\.([A-Z]+)", file)
    # and sets the match as the key for mcs
    mcs[m.group(1)] = MarkovChain(file)

  while True:
    try:
      # it used to be random. now with weights
      #name = random.choice(mcs.keys())
      name = weighted_choice([("CLINTON", 40), ("TRUMP", 40), ("HOLT", 8), ("COOPER", 8), ("RADDATZ", 8), ("WALLACE", 8)])
      if os.environ.get('SLACK_WEBHOOK'):
        # come back and add a webhook POSTer
        emoji_name = ":bot_" + name.lower() + ":"
        payload = {'username': name, 
                   'icon_emoji': emoji_name, 
                   'text': unicode(mcs[name].generateString(), 'utf-8')}
        r = requests.post(os.environ.get('SLACK_WEBHOOK'), data=json.dumps(payload))
        print(r, r.text)
      else:
        print(name +": "+ unicode(mcs[name].generateString(), 'utf-8'))
      time.sleep(15)
    except KeyboardInterrupt:
      sys.exit()
