"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from routes import Mapper

def make_map(config):
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False
    map.explicit = True
    
    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE
    map.connect('/map/systems', controller='map', action='systems')
    map.connect('/map/complete', controller='map', action='complete')
    
    map.connect('travel_index', '/travel', controller='travel', action='index')
    map.connect('/travel/{action}', controller='travel')
    map.connect('intel_index', '/intel', controller='intel', action='index')
    
    map.connect('latest.json', "/reports/latest.json", controller="reports", action="latest_reports")
    map.connect('check.json', "/reports/check.json", controller="reports", action="latest_check")
    
    map.connect("index", "/", controller="main", action="index")
    map.connect("help", "/help/", controller="main", action="help")

    map.resource("report", "reports")
    map.resource("hash", "hashes")
    map.resource("solarsystem", "solarsystems")

    map.connect("auth_signout", "/auth/signout", controller="auth", action="signout")
    map.connect("auth_signin", "/auth/signin", controller="auth", action="signin",
        conditions=dict(method=["GET"]))
    map.connect("/auth/signin", controller="auth", action="do_signin",
        conditions=dict(method=["POST"]))
    
    #map.connect("/solarsystems/current", controller="solarsystems", action="show")
    return map
