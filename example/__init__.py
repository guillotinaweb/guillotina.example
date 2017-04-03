from guillotina import configure
from guillotina.i18n import MessageFactory

# this is just setting up a convenience method for having i18n for
# strings and such. See http://docs.zope.org/zope.i18nmessageid/narr.html
# for maybe some insight into where this comes from in guillotina
_ = MessageFactory('example')


# this is a convention -- plone.server will see the includeme() method
# and call it for all registered applications
def includeme(root):
    # these, basically, load the specified module so that all the
    # decorators activate and configure application in various ways
    # (by defining services, behaviors, contenttypes, etc)
    configure.scan("example.behaviors")
    configure.scan("example.contenttypes")
    configure.scan("example.services")
