from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class NetsightArchetypes(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import netsight.archetypes
        xmlconfig.file('configure.zcml',
                       netsight.archetypes,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        pass

NETSIGHT_ARCHETYPES_FIXTURE = NetsightArchetypes()
NETSIGHT_ARCHETYPES_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(NETSIGHT_ARCHETYPES_FIXTURE, ),
                       name="NetsightArchetypes:Integration")