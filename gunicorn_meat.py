# -*- coding: utf-8 -*-

from gunicorn import util
from gunicorn.app.base import Application

class WSGIApp(Application):

    def __init__(self, application, options={}):
        """ Start the object. Default gUnicorn configuration is loaded """

        self.application = application
        self.usage = None
        self.callable = None
        self.options = options
        self.do_load_config()

    def init(self, parser, opts, args):
        """ Apply our custom settings """

        cfg = {}
        for k, v in self.options.items():
            if k.lower() in self.cfg.settings and v is not None:
                cfg[k.lower()] = v
        return cfg

    def load(self):
        """ Attempt an import of the specified application """

        if isinstance(self.application,str):
            return util.import_app(self.application)
        else:
            return self.application

class Meat(object):

    def __init__(self,app,**options):
        """ Assign our application """

        self.app = WSGIApp(app,options)

    def run(self):
        """ Run our application """

        self.app.run()