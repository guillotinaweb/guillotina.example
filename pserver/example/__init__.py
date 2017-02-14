from plone.server import configure
from zope.i18nmessageid import MessageFactory

# this is just setting up a convenience method for having i18n for
# strings and such. See http://docs.zope.org/zope.i18nmessageid/narr.html
_ = MessageFactory('pserver.example')


# this is a convention -- plone.server will see the includeme() method
# and call it for all registered applications
def includeme(root):
    # these, basically, load the specified module so that all the
    # decorators activate and configure application in various ways
    # (by defining services, behaviors, contenttypes, etc)
    configure.scan("pserver.example.behaviors")
    configure.scan("pserver.example.contenttypes")
    configure.scan("pserver.example.services")
