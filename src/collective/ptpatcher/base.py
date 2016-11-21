# coding=utf-8
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

import os


class PatchedViewPagetTemplateFile(ViewPageTemplateFile):

    def __init__(self, original, target, modifier, *args, **kwargs):
        ''' Test
        '''
        self.original = original
        self.modifier = modifier
        self.target = target
        self.patch()
        super(PatchedViewPagetTemplateFile, self).__init__(
            self.target,
            *args,
            **kwargs
        )

    def patch(self):
        '''
        '''
        modified = self.modifier(self.original)
        path = os.path.split(self.target)[0]
        if not os.path.exists(path):
            os.makedirs(path)
        with open(self.target, 'w') as ou:
            ou.write(modified)
