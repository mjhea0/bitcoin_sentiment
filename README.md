# Bitcoin Sentiment
### bitcoin sentiment analysis

#### Prereqs
- Mongodb and an instance running
  - sudo apt-get install mongodb
- virtualenvwrapper
  - sudo pip install virtualenvwrapper

#### How do you run it, you ask?
    mkvirtualenv bitcoin_sentiment  &&\
    pip -r install requirements.txt && \
    python manage.py runserver

#### Why is the requirements.txt file so large?
That's what she said. I forgot to use `--no-site-packages`, and this is me tinkering

#### TODO
- add tests
- add other sites
