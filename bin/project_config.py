import os
import sys
from configparser import ConfigParser
from definition import PROJECT_CONFIG


class ProjectConfig:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(PROJECT_CONFIG)
        try:
            self.set_host(os.environ['QA_host'])
        except KeyError:
            sys.exit("Can't find 'QA_host' in environment")

    def set_host(self, host):
        self.config['SERVER']['host'] = host

    @property
    def host(self):
        return self.config['SERVER']['host']

    @property
    def credentials(self):
        return self.config['CREDENTIALS']

    @property
    def database(self):
        return self.config['DB']


cfg = ProjectConfig()

