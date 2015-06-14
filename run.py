from chronos.web.app import app
from chronos.config import config


app.run(
    debug=config.flask.get('debug')
)
