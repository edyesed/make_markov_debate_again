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
      name = random.choice(mcs.keys())
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
      time.sleep(2)
    except KeyboardInterrupt:
      sys.exit()
