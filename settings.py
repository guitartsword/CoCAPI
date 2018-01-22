"""settings for each environment."""
import os
import json
ENV = os.environ.get('ENV')
with open('config_%s.json' % ENV) as config_data:
    SETTINGS = json.load(config_data)
