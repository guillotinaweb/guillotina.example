from guillotina import configure
from guillotina.behaviors.instance import AnnotationBehavior
from guillotina.interfaces import IFormFieldProvider, IResource
from zope.interface import Interface, provider, implementer
from guillotina.schema import TextLine

from example import _


# behaviors, interfaces, and adapters are all very much linked.
# SEE: https://zopeinterface.readthedocs.io/en/latest/

# for guillotina specific documentation on behaviors,
# SEE: http://guillotina.readthedocs.io/en/latest/developer/behavior.html


# This is saying that ICustomBehavior facilitates the IFormFieldProvider
# interface.
@provider(IFormFieldProvider)
# ICustomBehavior is an Interface that provides a type for defining
# the properties of a behavior
class ICustomBehavior(Interface):
    # ...and it provides the following attributes, which are intended
    # to be form fields (hence, this behavior _provides_ IFormFieldProvider)
    bar = TextLine(
        title=_(u'Bar'),
        required=True
    )


# This is an Interface that creates a type that can be used to _mark_
# objects as implementing the behavior
class IMarkerCustomBehavior(Interface):
    pass


# this is the actual definition of the behavior!
# this 'implementer' bit _should_ be automatic, and might be in a future update
# to guillotina, for now this explicitely states that the behavior implements
# the ICustomBehavior interface to the system.
@implementer(ICustomBehavior)
# SEE: http://guillotina.readthedocs.io/en/latest/developer/applicationconfiguration.html#behavior
@configure.behavior(
    title="CustomBehavior",
    # this class definition provides the behavioral implementation of
    # ICustomBehavior
    provides=ICustomBehavior,
    # the IMarkerCustomBehavior interface should be used to apply this behavior
    # to objects that desire it's features
    marker=IMarkerCustomBehavior,
    # content type this behavior is available for (as defined by it's Interface)
    # in this case, anything that is an IResource (which IItem is, and ICustomType
    # is an IItem)
    for_=IResource)
# the AnnotationBehavior parent basically puts all otherwise unhandled attribute
# data from the provided interfaces into annotation data on the object the
# behavior is associated with.
class CustomBehavior(AnnotationBehavior):
    pass
