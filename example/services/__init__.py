# TERMINOLOGY: "service" in this context is synonymous with "view" in many
# other frameworks

# see the aservice.py file for more detailed breakdown of service declaration
from . import aservice
from . import customtypeservice
from . import chainedservice

from guillotina import configure
from guillotina.api.service import Service
from guillotina.interfaces import IContainer
from guillotina.browser import Response



# this is an example of a service with a very custom response.
@configure.service(
    context=IContainer,
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
