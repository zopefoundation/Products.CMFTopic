##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" Unit test layers.
"""

from Testing import ZopeTestCase
ZopeTestCase.installProduct('ZCTextIndex', 1)
ZopeTestCase.installProduct('CMFCore', 1)

import transaction
from Zope2.App import zcml

from Products.CMFCore.testing import FunctionalZCMLLayer
from Products.CMFDefault.factory import addConfiguredSite


class FunctionalLayer(FunctionalZCMLLayer):

    @classmethod
    def setUp(cls):
        import Products.CMFTopic
        import Products.CMFDefault
        import Products.DCWorkflow

        zcml.load_config('configure.zcml', Products.CMFTopic)
        zcml.load_config('configure.zcml', Products.CMFDefault)
        zcml.load_config('configure.zcml', Products.DCWorkflow)

        app = ZopeTestCase.app()
        addConfiguredSite(app, 'site', 'Products.CMFDefault:default',
                          snapshot=False,
                          extension_ids=('Products.CMFTopic:default',))
        transaction.commit()
        ZopeTestCase.close(app)

    @classmethod
    def tearDown(cls):
        app = ZopeTestCase.app()
        app._delObject('site')
        transaction.commit()
        ZopeTestCase.close(app)
