# -*- coding: utf-8 -*-
from collective.ptpatcher.base import PatchedViewPagetTemplateFile
from collective.ptpatcher.testing import COLLECTIVE_PTPATCHER_INTEGRATION_TESTING  # noqa
from pkg_resources import resource_filename
from plone import api
from Products.Five import BrowserView

import unittest


def dummy_modifier(original):
    '''
    '''
    with open(original) as original:
        return original.read().capitalize()


class DummyView(BrowserView):
    ''' A view with a patched template
    '''

    index = PatchedViewPagetTemplateFile(
        original=resource_filename(
            'collective.ptpatcher',
            'tests/templates/a.pt',
        ),
        target=resource_filename(
            'collective.ptpatcher',
            'tests/ptpatcher/b.pt',
        ),
        modifier=dummy_modifier
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
