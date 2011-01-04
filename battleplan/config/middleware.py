"""Pylons middleware initialization"""
from beaker.middleware import SessionMiddleware
from paste.cascade import Cascade
from paste.registry import RegistryManager
from paste.urlparser import StaticURLParser
from paste.deploy.converters import asbool
from pylons.middleware import ErrorHandler, StatusCodeRedirect
from pylons.wsgiapp import PylonsApp
from routes.middleware import RoutesMiddleware

from battleplan.config.environment import load_environment

class EveState:
  def __init__(self, environ):
    self.trusted = "HTTP_EVE_TRUSTED" in environ and environ["HTTP_EVE_TRUSTED"] == "Yes"
    
    if self.trusted:
        self.char_id = int(environ["HTTP_EVE_CHARID"]);
        self.char_name = environ["HTTP_EVE_CHARNAME"];
        self.station_id = int(environ["HTTP_EVE_STATIONID"]);
        self.station_name = environ["HTTP_EVE_STATIONNAME"];
        self.corp_name = environ["HTTP_EVE_CORPNAME"];
        self.constellation_name = environ["HTTP_EVE_CONSTELLATIONNAME"];
        self.region_name = environ["HTTP_EVE_REGIONNAME"];
        self.solarsystem_name = environ["HTTP_EVE_SOLARSYSTEMNAME"];
    else:
        self.char_id = None;
        self.char_name = None;
        self.station_id = None;
        self.station_name= None;
        self.corp_name = None;
        self.constellation_name = None;
        self.region_name = None;
        self.solarsystem_name = None;
    
    if "HTTP_EVE_ALLIANCEID" in environ:
        self.alliance_id = int(environ["HTTP_EVE_ALLIANCEID"]);
        self.alliance_name = environ["HTTP_EVE_ALLIANCENAME"];
    else:
        self.alliance_id = None;
        self.alliance_name = None;

class EveMiddleware:
  def __init__(self, app, config):
    self.app = app
    self.config = config

  def __call__(self, environ, start_response):
    environ["eve"] = EveState(environ);
    return self.app(environ, start_response)

def make_app(global_conf, full_stack=True, static_files=True, **app_conf):
    """Create a Pylons WSGI application and return it

    ``global_conf``
        The inherited configuration for this application. Normally from
        the [DEFAULT] section of the Paste ini file.

    ``full_stack``
        Whether this application provides a full WSGI stack (by default,
        meaning it handles its own exceptions and errors). Disable
        full_stack when this application is "managed" by another WSGI
        middleware.

    ``static_files``
        Whether this application serves its own static files; disable
        when another web server is responsible for serving them.

    ``app_conf``
        The application's local configuration. Normally specified in
        the [app:<name>] section of the Paste ini file (where <name>
        defaults to main).

    """
    # Configure the Pylons environment
    config = load_environment(global_conf, app_conf)

    # The Pylons WSGI app
    app = PylonsApp(config=config)
    app = EveMiddleware(app, config)
    
    # Routing/Session/Cache Middleware
    app = RoutesMiddleware(app, config['routes.map'], singleton=False)
    app = SessionMiddleware(app, config)
    
    # CUSTOM MIDDLEWARE HERE (filtered by error handling middlewares)

    if asbool(full_stack):
        # Handle Python exceptions
        app = ErrorHandler(app, global_conf, **config['pylons.errorware'])

        # Display error documents for 401, 403, 404 status codes (and
        # 500 when debug is disabled)
        if asbool(config['debug']):
            app = StatusCodeRedirect(app)
        else:
            app = StatusCodeRedirect(app, [400, 401, 403, 404, 500])

    # Establish the Registry for this application
    app = RegistryManager(app)

    if asbool(static_files):
        # Serve static files
        static_app = StaticURLParser(config['pylons.paths']['static_files'])
        app = Cascade([static_app, app])
    app.config = config
    return app
