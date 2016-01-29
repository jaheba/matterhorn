
.. image:: logo.png
    :width: 200px

Matterhorn
~~~~~~~~~~

Matterhorn is a framework for writing integrations for the mattermost communication platform. It supports both incoming (`uphill`) and outgoing (`downhill`) webhooks.


Installation
============

::
    
    pip install matterhorn

Using plugins
=============

Example::

    from matterhorn import Matterhorn

    app = Matterhorn(__name__)

    app.add_plugin(
        name='github',
        url_prefix='/in/github',
        plugin='mm_github.github',
        url='http://chat.soft-dev.org/hooks/hrwtbj9db7dhbx9oza1bzi8tee'
    )


Writing plugins
===============

Matterhorn differs between up- and downhill message. Uphill messages are sent to
the mattermost server (incoming webhooks), whilst downhill messages are received
from mattermost (outgoing webhooks).

Matterhorn utilizes Flask's ``Blueprint`` feature to support multiple plugins for
a single application server.

uphill
------

Example::

    from flask import Blueprint
    from matterhorn import Uphill


    def make_blueprint(name):
        blueprint = Blueprint(name, __name__)

        spam = Uphill(
            username='spammer'
        )

        @blueprint.route('/<name>', methods=['GET'])
        def index(name):
            return spam.send('Hello %s!' %name)

        return blueprint, spam

downhill
--------

Example::

    from flask import Blueprint
    from matterhorn import Downhill

    def make_blueprint(name):
        blueprint = Blueprint(name, __name__)

        greeter = Downhill(
            blueprint=blueprint,
            username='greeter bot'
        )

        @syncbot
        def handle(message):
            return greeter.response('Hello %s!' %message.user_name)

        return blueprint, greeter