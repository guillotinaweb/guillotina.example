from guillotina import configure
from guillotina.api.service import Service
from guillotina.browser import Response

from example.contenttypes import ICustomType


@configure.service(
    context=ICustomType,
    name='@customtype',
    method='GET',
    permission='plone.AccessPreflight')
async def JSONResponseFunc(context, request):
    import pdb; pdb.set_trace()
    return {'foo':['bar','baz']}
