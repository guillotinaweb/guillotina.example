# TERMINOLOGY: "service" in this context is synonymous with "view" in many
# other frameworks

# see the aservice.py file for more detailed breakdown of service declaration
from . import aservice
from . import customtypeservice
from . import chainedservice

from plone.server import configure
from plone.server.api.service import Service
from plone.server.interfaces import ISite
from plone.server.browser import Response



# this is an example of a service with a very custom response.
@configure.service(
    context=ISite,
    name='@exampleservice',
    method='GET',
    permission='plone.AccessPreflight')
class ExampleService(Service):
    async def __call__(self):
        return Response(response='some <strong>html</strong>',
                        headers={
                            "Content-Type": "text/html"
                        },
                        status=200)
