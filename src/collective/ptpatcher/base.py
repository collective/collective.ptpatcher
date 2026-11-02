from importlib.resources import files
from logging import getLogger
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

import os


class BasePatcher:

    logger = getLogger(__name__)

    def __init__(self, source, target):
        """Base class for patching templates."""
        if isinstance(source, tuple):
            source = str(files(source[0]).joinpath(source[1]))
        if isinstance(target, tuple):
            target = str(files(target[0]).joinpath(target[1]))
        self.source = source
        self.target = target

    @property
    def name(self):
        """Used for logging"""
        return self.__class__

    def as_index(self, *args, **kwargs):
        """Return the view page template file to be used as an index"""
        if not os.path.exists(self.target) or os.path.getmtime(
            self.source
        ) > os.path.getmtime(self.target):
            self.apply_patch()
        return ViewPageTemplateFile(self.target)

    def get_patched(self):
        """The method used for patching"""
        raise RuntimeError("Not implemented yet")

    def apply_patch(self):
        """Patch the original and save it to the target."""
        self.logger.info(
            "%r:\n\tSource:\t%s\n\tTarget:\t%s",
            self.name,
            self.source,
            self.target,
        )
        path = os.path.split(self.target)[0]
        if not os.path.exists(path):
            os.makedirs(path)
        with open(self.target, "w") as ou:
            patched = self.get_patched()
            ou.write(patched.decode("utf8") if isinstance(patched, bytes) else patched)
        return self
