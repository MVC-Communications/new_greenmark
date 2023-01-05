import os
import sys
from greenmark.wsgi import application
# sys.path.insert(0,os.path.dirname(__file__))

# environ = os.environ.setdefault("DJANGO_SETTINGS_MODULE", "greenmark.settings")



# cwd = os.getcwd()
# sys.path.append(cwd)
# sys.path.append(cwd + '/myapp')
# SCRIPT_NAME = os.getcwd()
# class PassengerPathInfoFix(object):
#     def __init__(self, app):
#         self.app = app

#     def __call__(self, environ, start_response):
#         from urllib.parse import unquote
#         environ['SCRIPT_NAME'] = SCRIPT_NAME
#         request_uri = unquote(environ['REQUEST_URI'])
#         script_name = unquote(environ.get('SCRIPT_NAME', ''))
#         offset = request_uri.startswith(script_name) and len(environ['SCRIPT_NAME']) or 0
#         environ['PATH_INFO'] = request_uri[offset:].split('?', 1)[0]
#         return self.app(environ, start_response)

# application = PassengerPathInfoFix(application)