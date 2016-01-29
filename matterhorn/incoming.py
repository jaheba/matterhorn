

'''
Incoming Webhooks
~~~~~~~~~~~~~~~~~

Provides API for `uphill` messages.

'''

import json
import requests

from .core import HillBase

class Uphill(HillBase):
    def __init__(self, url=None, channel=None, username=None, icon_url=None):
        self.matterhorn_config = {}
        self.defaults = {
            'channel': channel,
            'username': username,
            'icon_url': icon_url
        }

    def _update_payload(self, payload, options):
        for option in 'channel', 'username', 'icon_url':
            value = self._get_option(option, options)
            if value is not None:
                payload[option] = value

        return payload

    def send(self, message, hook_data=None, **options):
        payload = self._update_payload({
            'text': message 
        }, options)

        req = requests.post(
            self._get_option('url'),
            headers={'Content-Type': 'application/json'},
            data=json.dumps(payload),
            verify=False)

        if req.status_code is not requests.codes.ok:
            print 'Error'

        return 'ok'


