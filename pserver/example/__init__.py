from plone.server import configure
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('pserver.example')


def includeme(root):
    configure.scan("pserver.example.services")
