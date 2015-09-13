from setuptools import setup
import os


setup(name='test-pkg',
      version="1.0",
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      description='Application for testing CI',
      long_description="",
      author='Robert Weidlich',
      author_email='portal@robertweidlich.de',
      url='https://github.com/cato-/test',
      packages=['testpkg'],
      include_package_data=True,
      classifiers=[
          ],
      )
