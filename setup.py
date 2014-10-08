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

setup(name='abbreviate',
		version=__version__,
		description="Automatically abbreviate text",
		long_description=readme(),
		classifiers=[
			"Development Status :: 3 - Alpha",
			"Intended Audience :: Developers",
			"Programming Language :: Python",
			"License :: OSI Approved :: MIT License",
			"Natural Language :: English",
			"Topic :: Text Processing :: Filters",
			],
		keywords='string formatting',
		author="Pat Pannuto",
		author_email="pat.pannuto+abbreviate@gmail.com",
		url="https://github.com/ppannuto/python-abbreviate",
		license="MIT",
		packages=find_packages(),
		package_data={'': ['*.abbr']},
		include_package_data=True,
		zip_safe=False,
		install_requires=requires,
		#entry_points = {
		#    'console_scripts':['abbreviate = abbreviate:console']
		#},
		)

