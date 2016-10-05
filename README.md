# -_make_markov_debate_again_-
Who doesn't love a markovbot seeded with a transcript of the presidential debate?

# I do


# To run
0. `virtualenv ~/virtualenvs/markov`
1. `source ~/virtualenvs/markov/bin/activate`
1. `pip install -f requirements.txt`
2. `./parse_transcript_markov.py`
3. 
    ```python
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
