from requests import get
from mongoengine import * # go crazy!
from bitcoin_sentiment import models
from time import strftime, strptime
from dateutil import parser

connect('bitcoin_sentiment')

# For this simple app, I'll just fetch some data from twitter, but I might add in another source afterward
sites = [{'twitter': 'http://search.twitter.com/search.json?q=bitcoin'}]
sitesData = []

def fetch_sentiment(sites):
    for site in sites:
        for key, val in site.iteritems():
            receivedData = {}
            receivedData[key] = get(val).json()
            sitesData.append(receivedData)

def fetch_twitter_data():
    fetch_sentiment(sites)
    for site in sitesData:
        for data in site['twitter']['results']:
            if not (data_duplicate(data['id'])):
                store_message(data)

def data_duplicate(identifier):
    if (models.Message.objects(msg_id= identifier)):
        return True
    else: return False
     
def store_message(data):
    msg = models.Message(
        created_at = date_field_time(data['created_at']),
        from_user = data['from_user'],
        from_user_id = data['from_user_id'],
        msg_id = data['id'],
        msg_lang = data['iso_language_code'],
        msg_text = data['text'],)
    msg.save()

def date_field_time(data):
    timestamp = strftime('%Y-%m-%d %H:%M:%S', strptime(data,'%a, %d %b %Y %H:%M:%S +0000'))
    return parser.parse(timestamp)


fetch_twitter_data()
