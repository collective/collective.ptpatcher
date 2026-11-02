from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneWithPackageLayer

import collective.ptpatcher.tests

COLLECTIVE_PTPATCHER_FIXTURE = PloneWithPackageLayer(
    zcml_package=collective.ptpatcher.tests,
    zcml_filename="configure.zcml",
    name="CollectivePtpatcher:Fixture",
)

COLLECTIVE_PTPATCHER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_PTPATCHER_FIXTURE,),
    name="CollectivePtpatcherLayer:IntegrationTesting",
)
