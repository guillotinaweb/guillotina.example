from plone.server import configure
from plone.server.api.service import Service
from plone.server.browser import Response

from pserver.example.contenttypes import ICustomType


@configure.service(
    context=ICustomType,
    name='@customtype',
    method='GET',
    permission='plone.AccessPreflight')
async def JSONResponseFunc(context, request):
    import pdb; pdb.set_trace()
    return {'foo':['bar','baz']}
