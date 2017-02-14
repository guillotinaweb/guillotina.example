from plone.server import configure
from plone.server.content import Item
from plone.server.interfaces import IItem
from zope import schema


# the `IItem` type describes an object that is pretty basic, defining the
# following (relevant) properties about the object:
#   - it is containable (IContained is a parent)
#   - it is a resource (IResource is a parent)
#   - it has a 'portal_type' property (from IResource)
#   - it has a 'title' property (from IResource)
class ICustomType(IItem):
    # SEE: http://docs.zope.org/zope.schema/narr.html for more info about
    # zope.schema
    foo = schema.Text()


# SEE: http://ploneserver.readthedocs.io/en/latest/applicationconfiguration.html#content-type
@configure.contenttype(
    portal_type="CustomType",
    schema=ICustomType,
    # behaviors are a part of a larger subject that includes the concept of
    # Interfaces and Adapters. In this case, you can think of behviors
    # as ways to include features from other object definitions as features
    # associated with this type. IE pserver.example.behaviors.ICustomBehavior
    # defines some properties that are useful for a CustomType object to have.
    # SEE: http://ploneserver.readthedocs.io/en/latest/behavior.html
    behaviors=[
        # the IDublinCore is a schema based on the Dublin Core meta data
        # specification. In this case, it adds fields like "creators",
        # "contributors", "created", and "modified" to the type.
        "plone.server.behaviors.dublincore.IDublinCore",
        # ICustomBehavior is, in this case, just an example of how to create
        # and use a custom behavior. It provides the "bar" field
        "pserver.example.behaviors.ICustomBehavior",
    ])
# an Item is the most basic type pre-defined in plone.server and doesn't come
# with much baggage beyond a 'title' property -- it knows how to setup ACL,
# identify itself, manage creation and modification dates, etc.
#
# the other basic type that you may see often is "plone.server.content.Folder"
# which is similar to "Item" but understands how to contain other content types
# (where Item just understands how to _be_ contained)
class CustomType(Item):
    pass
