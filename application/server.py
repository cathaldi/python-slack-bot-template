from flask import Flask, request
import os
from slackclient import SlackClient

app = Flask(__name__)

# SLACK_CHANNEL_ID = ''


sc = SlackClient(os.environ.get("SLACK_BOT_OAUTH"))

@app.route('/test_endpoint', methods=['GET'])
def test():
    if request.json.get("type") == 'url_verification':
        return request.json.get("challenge")
