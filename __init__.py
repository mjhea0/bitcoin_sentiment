from flask import Flask
from flask.ext.mongoengine import MongoEngine
# from bitcoin_sentiment import twitter_feed
import sched, time

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': 'bitcoin_sentiment'}
app.config["SECRET_KEY"] = 'sloopersecret'
app.debug = True

db = MongoEngine(app)

if __name__ == '__main__':
    app.run()
    grab_twitter_data_repeatedly()

def register_blueprints(app):
    # Prevents circular imports
    from bitcoin_sentiment.views import messages
    app.register_blueprint(messages)

def grab_twitter_data_repeatedly():
    s = sched.scheduler(time.time, time.sleep)
    # update every 5 minutes
    s.enter(300, 1, twitter_feed.fetch_twitter_data(), (s,))
    s.run()

register_blueprints(app)
