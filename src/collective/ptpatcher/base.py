# coding=utf-8
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

import os


class BasePatchedPTFile(ViewPageTemplateFile):

    def __init__(self, original, target, *args, **kwargs):
        ''' Base class for pathcing templates
        '''
        self.original = original
        self.target = target
        self.patch()
        super(BasePatchedPTFile, self).__init__(
            self.target,
            *args,
            **kwargs
        )

    def create_target(self):
        ''' The method used for patching
        '''
        raise RuntimeError('Not implemented yet')

    def patch(self):
        ''' Path orginal and save it to target
        '''
        path = os.path.split(self.target)[0]
        if not os.path.exists(path):
            os.makedirs(path)
        with open(self.target, 'w') as ou:
            ou.write(self.create_target())
