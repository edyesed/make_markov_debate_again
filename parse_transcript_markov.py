#!/usr/bin/env python
#
import re
# 
# It would be super cool to grab the transcript hot via requests, 
#   but I didn't do that. This one was cut+pasted, and it needed a little
#   cleanup to remove annotations from the source
#import requests
#from bs4 import BeautifulSoup as bs
from pymarkovchain import MarkovChain
#from pprint import pprint

FILE='./transcript.pres.v1'

def main():
  re_speaker_text = re.compile(r"^([A-Z]+): (.*)", re.MULTILINE)
  with open(FILE, 'r') as content_file:
    content = content_file.read()
  for match in re_speaker_text.finditer(content):
    speaker, said = match.groups()
    mc = MarkovChain("/var/tmp/markov_db.{0}".format(speaker))
    mc.generateDatabase(said.lower())
    mc.dumpdb()
 

if __name__ == "__main__":
  main()
