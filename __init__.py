from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': 'bitcoin_sentiment'}
app.config["SECRET_KEY"] = 'sloopersecret'
app.debug = True

db = MongoEngine(app)

if __name__ == '__main__':
    app.run()

def register_blueprints(app):
    # Prevents circular imports
    from bitcoin_sentiment.views import messages
    app.register_blueprint(messages)

register_blueprints(app)
