import os
import sys

from setuptools import setup, find_packages

def readme():
	with open('README.rst') as f:
		return f.read()

from abbreviate import __version__

requires = [
		'pyenchant',
		]

setup(
		name='abbreviate',
		version=__version__,
		#
		packages=find_packages(exclude=['tests']),
		package_data={'': ['*.abbr']},
		#
		description="Automatically abbreviate text",
		long_description=readme(),
		#
		url="https://github.com/ppannuto/python-abbreviate",
		#
		author="Pat Pannuto",
		author_email="pat.pannuto+abbreviate@gmail.com",
		#
		license="MIT",
		#
		classifiers=[
			"Development Status :: 3 - Alpha",
			"Intended Audience :: Developers",
			"Programming Language :: Python",
			"License :: OSI Approved :: MIT License",
			"Natural Language :: English",
			"Topic :: Text Processing :: Filters",
			],
		#
		keywords='string formatting',
		#
		install_requires=requires,
		include_package_data=True,
		zip_safe=False,
		#
		test_suite='abbreviate.tests',
		#
		#entry_points = {
		#    'console_scripts':['abbreviate = abbreviate:console']
		#},
		)

