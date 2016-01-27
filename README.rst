
matterhorn
~~~~~~~~~~

`matterhorn` is a framework for writing integrations for the mattermost communication platform. It supports both incoming (`uphill`) and outgoing (`downhill`) webhooks.


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