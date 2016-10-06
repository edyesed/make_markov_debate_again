#!/usr/bin/env python
#
import re
# 
# It would be super cool to grab the transcript hot via requests, 
#   but I didn't do that. This one was cut+pasted, and it needed a little
#   cleanup to remove annotations from the source
from io import open

FILE='./transcript.pres.v1'

def main():
  re_speaker_text = re.compile(r"^([A-Z]+): (.*)", re.MULTILINE)
  with open(FILE, 'r') as content_file:
    content = content_file.read()
  for match in re_speaker_text.finditer(content):
    speaker, said = match.groups()
    # I know, so expensive
    f = open('./training_texts/{0}.text'.format(speaker), encoding='utf-8', mode='a')
    f.write(said + "\n")
    f.close()

if __name__ == "__main__":
  main()
