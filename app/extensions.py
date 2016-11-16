import os

from flask_migrate import Migrate
migrate = Migrate()

elasticsearch_url = ELASTICSEARCH_URL = os.environ.get(
        'ELASTICSEARCH_URL',
        'http://localhost:9200/',
    )
