from guillotina import configure
from guillotina.content import Item
from guillotina.interfaces import IItem
from guillotina import schema


# the `IItem` type describes an object that is pretty basic, defining the
# following (relevant) properties about the object:
#   - it is containable (IContained is a parent)
#   - it is a resource (IResource is a parent)
#   - it has a 'portal_type' property (from IResource)
#   - it has a 'title' property (from IResource)
class ICustomType(IItem):
    # SEE: http://docs.zope.org/zope.schema/narr.html for more insight about
    # zope.schema, which relates to what guillotina.schema does
    foo = schema.Text()


# SEE: http://guillotina.readthedocs.io/en/latest/developer/applicationconfiguration.html#content-type
@configure.contenttype(
    type_name="CustomType",
    schema=ICustomType,
    # behaviors are a part of a larger subject that includes the concept of
    # Interfaces and Adapters. In this case, you can think of behviors
    # as ways to include features from other object definitions as features
    # associated with this type. IE example.behaviors.ICustomBehavior
    # defines some properties that are useful for a CustomType object to have.
    # SEE: http://guillotina.readthedocs.io/en/latest/developer/behavior.html
    behaviors=[
        # the IDublinCore is a schema based on the Dublin Core meta data
        # specification. In this case, it adds fields like "creators",
        # "contributors", "created", and "modified" to the type.
        "guillotina.behaviors.dublincore.IDublinCore",
        # ICustomBehavior is, in this case, just an example of how to create
        # and use a custom behavior. It provides the "bar" field
        "example.behaviors.ICustomBehavior",
    ])
# an Item is the most basic type pre-defined in guillotina and doesn't come
# with much baggage beyond a 'title' property -- it knows how to setup ACL,
# identify itself, manage creation and modification dates, etc.
#
# the other basic type that you may see often is "guillotina.content.Folder"
# which is similar to "Item" but understands how to contain other content types
# (where Item just understands how to _be_ contained)
class CustomType(Item):
    pass
