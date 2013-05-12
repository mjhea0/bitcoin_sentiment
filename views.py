from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from bitcoin_sentiment.models import Message

messages = Blueprint('messages', __name__, template_folder='templates')

class ListView(MethodView):
    def get(self):
        messages = Message.objects.all()
        return render_template('messages/list.html', messages=messages)

messages.add_url_rule('/', view_func=ListView.as_view('list'))
