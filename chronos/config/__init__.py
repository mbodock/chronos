import os

module_name = os.getenv('APP_ENV', 'dev')
config = __import__(module_name, globals(), level=1)
