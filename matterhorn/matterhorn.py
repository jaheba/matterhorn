
from flask import Flask

class Matterhorn(Flask):

    def add_plugin(self, name, url_prefix, plugin, **options):
        try:
            m = __import__(plugin, fromlist=['github'])
            make_blueprint = getattr(m, 'make_blueprint')
            blueprint, plugin = make_blueprint(name)
        except ImportError:
            raise

        plugin.matterhorn_config = options
        self.register_blueprint(blueprint, url_prefix=url_prefix)