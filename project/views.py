from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='home')
def hello(request):
    return Response('<a href="/myroute">click</a>')


listitems = ("firstli", "secondli", "thirdli")
urls = ("fst", "sec", "trd")
tuples = [p for p in zip(listitems, urls)]

@view_config(route_name='myroute', renderer='templates/index.pt')
def myroute(request):
    cont = "some content"
    return {'content' : cont, 'tuples': tuples}

@view_config(route_name='spec-route', renderer='templates/index.pt')
def art_desc(request):
    current = request.matchdict.get('sub')

    cont = "some spec content"
    return {'content' : cont, 'tuples': tuples, 'current_spec': current}

