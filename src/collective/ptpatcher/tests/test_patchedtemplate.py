# -*- coding: utf-8 -*-
from collective.ptpatcher.base import BasePatchedPTFile
from collective.ptpatcher.testing import COLLECTIVE_PTPATCHER_INTEGRATION_TESTING  # noqa
from pkg_resources import resource_filename
from plone import api
from Products.Five import BrowserView

import unittest


class DummyPatchedPTFile(BasePatchedPTFile):
    ''' Dummy pathcer for testing purpose
    '''
    def create_target(self):
        ''' A patcher that capitalizes text
        '''
        with open(self.original) as original:
            return original.read().capitalize()


class DummyView(BrowserView):
    ''' A view with a patched template
    '''

    index = DummyPatchedPTFile(
        original=resource_filename(
            'collective.ptpatcher',
            'tests/templates/a.pt',
        ),
        target=resource_filename(
            'collective.ptpatcher',
            'tests/ptpatcher/b.pt',
        ),
    )


class TestSetup(unittest.TestCase):
    '''Test that collective.ptpatcher is properly installed.'''

    layer = COLLECTIVE_PTPATCHER_INTEGRATION_TESTING

    def setUp(self):
        '''Custom shared utility setup for tests.'''
        self.portal = self.layer['portal']
        self.request = self.layer['request']

    def test_patch(self):
        '''Test that ICollectivePtpatcherLayer is registered.'''
        view = api.content.get_view(
            'test-ptpatcher',
            self.portal,
            self.request.clone(),
        )
        self.assertEqual(
            view(),
            u'Hello world!\n',
        )
