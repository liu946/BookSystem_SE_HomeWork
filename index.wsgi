import sae
from bookmanagement import wsgi

application = sae.create_wsgi_app(wsgi.application)