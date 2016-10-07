# -_make_markov_debate_again_-
Who doesn't love a markovbot seeded with a transcript of the presidential debate?

# I do
0. Politico
1. latimes
3. http://www.realclearpolitics.com/
4. https://www.hillaryclinton.com/speeches/


# To run (easy, slack)
0. Setup an incoming webhook. note the URL
0. `docker build -t pyapp:1 .`
1. `docker run -e "SLACK_WEBHOOK=url_from_above" -it pyapp:1`

# To run (easy, local)
0. `docker build -t pyapp:1 .`
1. `docker run -it pyapp:1`

# To run (hard)
0. `virtualenv ~/virtualenvs/markov`
1. `source ~/virtualenvs/markov/bin/activate`
1. `pip install -f requirements.txt`
2. `./parse_transcript_markov.py`
3. 

      ```
python
HOLT = MarkovChain('/var/tmp/markov_db.HOLT')
CLINTON = MarkovChain('/var/tmp/markov_db.CLINTON')
TRUMP = MarkovChain('/var/tmp/markov_db.TRUMP')
print(unicode(TRUMP.generateString(), 'utf-8'))
print(unicode(TRUMP.generateStringWithSeed("she"), 'utf-8'))
#she wins, i will bring back law and order
print(unicode(TRUMP.generateStringWithSeed("she"), 'utf-8'))
#she has experience, i agree
print(unicode(TRUMP.generateStringWithSeed("she"), 'utf-8'))
#she wins, i will absolutely support her
print(unicode(TRUMP.generateStringWithSeed("she"), 'utf-8'))
#she wins, i will tell you
print(unicode(TRUMP.generateStringWithSeed("she"), 'utf-8'))
#she wins, i will absolutely support her
print(unicode(TRUMP.generateStringWithSeed("she"), 'utf-8'))
#she wins, i will absolutely support her

```
