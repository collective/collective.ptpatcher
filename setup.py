"""Installer for the collective.ptpatcher package."""

from setuptools import setup

long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="collective.ptpatcher",
    version="1.0.1.dev0",
    description="Patch page templates in a sane way",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Operating System :: OS Independent",
    ],
    keywords="Python Plone",
    author="Alessandro Pisa",
    author_email="alessandro.pisa@gmail.com",
    url="https://pypi.python.org/pypi/collective.ptpatcher",
    project_urls={"Homepage": "https://github.com/collective/collective.ptpatcher"},
    python_requires=">=3.11",
    license_expression="GPL-2.0-only",
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Products.CMFPlone",
        "Zope",
        "zope.i18nmessageid",
        "zope.interface",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            "plone.app.contenttypes",
            "plone.app.robotframework",
            "plone.api",
            "lxml",
            "PyQuery",
            "z3c.jbot",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
