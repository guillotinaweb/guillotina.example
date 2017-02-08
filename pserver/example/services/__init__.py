from plone.server import configure
from plone.server.api.service import Service
from plone.server.interfaces import ISite
from plone.server.browser import Response


@configure.service(
    context=ISite,
    name='@exampleservice',
    method='GET',
    permission='plone.NotAuthenticated')
class ExampleService(Service):
    async def __call__(self):
        return Response(response='some <strong>html</strong>',
                        headers={
                            "Content-Type": "text/html"
                        },
                        status=200)
