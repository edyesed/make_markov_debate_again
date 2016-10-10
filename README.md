# -_make_markov_debate_again_-
Who doesn't love a markovbot seeded with a transcript of the presidential debate?  *I do*

# from dockerhub
0. all texts:  [docker pull edyesed/make_markov_debate_again](https://hub.docker.com/r/edyesed/make_markov_debate_again/)
0. just the debates: [docker pull edyesed/make_markov_debate_again:debate_latest](https://hub.docker.com/r/edyesed/make_markov_debate_again/tags/)

# Reference materials for the text
=======
0. Politico
1. latimes
3. http://www.realclearpolitics.com/
4. https://www.hillaryclinton.com/speeches/

# to run ( easiest, slack )
0. Setup an incoming webhook. note the URL
1. `docker pull edyesed/make_markov_debate_again`
1. `docker run -e "SLACK_WEBHOOK=url_from_above" -it edyesed/make_markov_debate_again`

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
1. `pip install -r requirements.txt`
2. `./parse_transcript_markov.py`
3. `./back-and-forth.py`
