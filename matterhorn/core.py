

class HillBase(object):

    def _get_option(self, key, options=None):
        for dictionary in options or {}, self.matterhorn_config, self.defaults:
            value = dictionary.get(key, None)
            if value is not None:
                return value
