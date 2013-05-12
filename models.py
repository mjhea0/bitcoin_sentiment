import datetime
from flask import url_for
from bitcoin_sentiment import db

class Message(db.DynamicDocument):
    meta = {'collection': 'bitcoin_sentiment_messages'}
    created_at = db.DateTimeField(required=True)
    from_user = db.StringField(max_length=255, required=True)
    from_user_id = db.FloatField(required=True)
    msg_id =  db.FloatField(required=True)
    msg_lang = db.StringField(max_length=255, required=True)
    msg_text = db.StringField(required=True)
    new = db.BooleanField(required=True)

    def get_absolute_url(self):
        return url_for('post', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.msg_text

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }
