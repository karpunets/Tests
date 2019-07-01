from configparser import ConfigParser
from definition import PROJECT_CONFIG


class ProjectConfig():
    def __init__(self, host):
        self.config = ConfigParser()
        self.config.read(PROJECT_CONFIG)
        self.config['SERVER']['host'] = host

    @property
    def host(self):
        return self.config['SERVER']['host']


cfg = ProjectConfig('http://10.100.70.17:8080')
print(cfg.host)