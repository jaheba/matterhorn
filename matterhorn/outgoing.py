

from collections import namedtuple

Message = namedtuple('Message', [
    'channel_id',
    'channel_name',
    'team_domain',
    'team_id',
    'text',
    'timestamp',
    'user_id',
    'user_name',
    'trigger_word'
])

# receiving messages from mattermost

from flask import request

from core import HillBase

class Downhill(HillBase):
    def __init__(self, blueprint, token=None, username=None, icon_url=None):
        # config is overriten by matterhorn later
        self.matterhorn_config = {}

        self.blueprint = blueprint
        self.token = token

        self.defaults = {
            'token': token,
            'username': username,
            'icon_url': icon_url
        }

        self.callback = None

        blueprint.route('/', methods=['POST'])(self._receive)

    def _receive(self):
        data = request.form
        print data

        if data.get('token', None) != self._get_option('token'):
            print 'Invalid TOKEN'
            return 'Invalid Token', 400

        msg = Message(
            data['channel_id'],
            data['channel_name'],
            data['team_domain'],
            data['team_id'],
            data['text'],
            data['timestamp'],
            data['user_id'],
            data['user_name'],
            data['trigger_word']
        )

        return self.callback(msg)

    def __call__(self, callback):
        self.callback = callback