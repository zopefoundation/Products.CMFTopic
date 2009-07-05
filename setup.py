import os
from setuptools import setup
from setuptools import find_packages

NAME = 'CMFTopic'

here = os.path.abspath(os.path.dirname(__file__))
package = os.path.join(here, 'Products', NAME)

def _package_doc(name):
    f = open(os.path.join(package, name))
    return f.read()

_boundary = '\n' + ('-' * 60) + '\n\n'
README = ( _package_doc('README.txt')
         + _boundary
         + _package_doc('CHANGES.txt')
         + _boundary
         + "Download\n========"
         )

setup(name='Products.%s' % NAME,
      version=_package_doc('version.txt').strip(),
      description='Topic product for the Zope Content Management Framework',
      long_description=README,
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Zope Public License",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        ],
      keywords='web application server zope zope2 cmf',
      author="Zope Corporation and contributors",
      author_email="zope-cmf@zope.org",
      url="http://pypi.python.org/pypi/Products.CMFTopic",
      license="ZPL 2.1 (http://www.zope.org/Resources/License/ZPL-2.1)",
      packages=find_packages(),
      include_package_data=True,
      namespace_packages=['Products'],
      zip_safe=False,
      setup_requires=['eggtestinfo',
                     ],
      install_requires=[
          'setuptools',
          #'Zope2 >= 2.10.4',
          'Products.CMFCore',
          'Products.CMFDefault',
          'Products.GenericSetup',
          ],
      tests_require=[
          'zope.testing >= 3.7.0',
          'Products.DCWorkflow',
          ],
      extras_require = dict(
          test = ['Products.DCWorkflow'],
          ),
      test_loader='zope.testing.testrunner.eggsupport:SkipLayers',
      test_suite='Products.%s.tests' % NAME,
      entry_points="""
      [zope2.initialize]
      Products.%s = Products.%s:initialize
      [distutils.commands]
      ftest = zope.testing.testrunner.eggsupport:ftest
      """ % (NAME, NAME),
      )
