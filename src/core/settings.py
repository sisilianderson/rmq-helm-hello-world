from environs import Env


class Settings(object):
    def __init__(self):
        env = Env()
        env.read_env()

        self.RMQ_SETTINGS = {
            'dsn': env.str('RMQ_DSN', 'localhost'),
        }