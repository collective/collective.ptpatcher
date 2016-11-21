# -*- coding: utf-8 -*-
from collective.ptpatcher.base import BasePatchedPTFile
from collective.ptpatcher.testing import COLLECTIVE_PTPATCHER_INTEGRATION_TESTING  # noqa
from pkg_resources import resource_filename
from plone import api
from Products.CMFPlone.browser.admin import Overview
from Products.Five import BrowserView
from pyquery import PyQuery as pq

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
            'tests/templates/hello_world.pt',
        ),
        target=resource_filename(
            'collective.ptpatcher',
            'tests/ptpatcher/hello_world.pt',
        ),
    )


class DummyXMLPatchedPTFile(BasePatchedPTFile):
    ''' Dummy pathcer for testing purpose
    '''
    def create_target(self):
        ''' A patcher that capitalizes text
        '''
        obj = pq(filename=self.original)
        header = obj('h1')[0]
        pq(header).after('<p>${python:len(sites)} sites created</p>')
        return str(obj)


class PatchedOverview(Overview):
    ''' Patched Plone overview
    '''

    index = DummyXMLPatchedPTFile(
        original=resource_filename(
            'Products.CMFPlone.browser',
            'templates/plone-overview.pt',
        ),
        target=resource_filename(
            'collective.ptpatcher',
            'tests/ptpatcher/plone-overview.pt',
        ),
    )


class TestSetup(unittest.TestCase):
    '''Test that collective.ptpatcher is properly installed.'''

    layer = COLLECTIVE_PTPATCHER_INTEGRATION_TESTING

    def setUp(self):
        '''Custom shared utility setup for tests.'''
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']

    def test_dummy_patch(self):
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

    def test_xml_patch(self):
        view = api.content.get_view(
            'test-patched-plone-overview',
            self.app,
            self.request.clone(),
        )
        self.assertIn(
            u'<p>1 sites created</p>',
            view(),
        )
