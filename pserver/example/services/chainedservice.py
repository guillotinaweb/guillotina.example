from plone.server import configure
from plone.server.api.service import Service
from plone.server.interfaces import ISite
from plone.server.browser import Response

# SEE the official services documentation for more info:
# http://ploneserver.readthedocs.io/en/latest/services.html
#
# also check out the other services, IE the ones in pserver.example.services.aservice
# and pserver.example.services.customtypeservice

# If you want to be able to have 1 function handle more than one HTTP method,
# it's really simple! Just chain decorators -- and give each method it's own
# properties (like, say, permissions!)

# this decorator is declaring the '@chained' service as a GET allowable
# by anyone with access to the service
@configure.service(
    context=ISite,
    name='@chained',
    method='GET',
    permission='plone.AccessPreflight')
# this one is declaring the '@chained' operator again, with a different HTTP
# method ('POST'), and restricting access to any user that has the plone.AddContent
# role
#
# this means that GET and POST are both handled by the same code, and have the
# same endpoint (and don't _need_ to), but are configured with different
# permissions that you don't have to check yourself inside the
# handler/service/view!!
#
# you could chain as many services definitions like this as you want!
# Alternatively, you don't have to chain _any_ services definitions -- each
# could be it's very own callable.
@configure.service(
    context=ISite,
    name='@chained',
    method='POST',
    permission='plone.AddContent')
class JSONResponse(Service):
    async def __call__(self):
        context = self.context
        request = self.request

        if request.method.upper() == "GET":
            return dict(msg="this was a GET message")
        else:
            return dict(msg="this was a POST message")
