from pyramid.config import Configurator

def main():
    """ This returns a Pyramid WSGI application.
    """
    with Configurator() as conf:
        conf.include('pyramid_chameleon')
        conf.add_route('home', '/')
        conf.add_route('myroute', '/myroute')
        conf.add_route('spec-route', '/myroute/{sub}')
        conf.scan()
        return conf.make_wsgi_app()
