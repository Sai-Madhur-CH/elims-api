import gunicorn.app.base
from gunicorn.workers import ggevent
from app import app
import multiprocessing


def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1

class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


if __name__ == '__main__':
    options = {
        'bind': '%s:%s' % (app.config['HOST'], app.config['PORT']),
        'worker_class': "gunicorn.workers.ggevent.GeventWorker",
        'log_level': 'info',
        'workers':number_of_workers(),
        'timeout':400
    }
    StandaloneApplication(app, options).run()