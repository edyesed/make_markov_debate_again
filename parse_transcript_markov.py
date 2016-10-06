#!/usr/bin/env python
#
import re
# 
# It would be super cool to grab the transcript hot via requests, 
#   but I didn't do that. This one was cut+pasted, and it needed a little
#   cleanup to remove annotations from the source
#import requests
#from bs4 import BeautifulSoup as bs
import glob
from pymarkovchain import MarkovChain
#from pprint import pprint

def main():
  #re_speaker_text = re.compile(r"^([A-Z]+): (.*)", re.MULTILINE)
  files = glob.glob("./training_texts/*")
  for file in files: 
    content = open(file).read()
    m = re.search("./training_texts/([A-Z]+)", file)
    speaker = m.group(1)
    mc = MarkovChain("/var/tmp/markov_db.{0}".format(speaker))
    mc.generateDatabase(content)
    mc.dumpdb()
 

if __name__ == "__main__":
  main()
