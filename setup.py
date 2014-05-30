from setuptools import setup
from sys import version_info
from pypuppetdb_daily_report import VERSION

pyver_requires = ['pypuppetdb>=0.1.0, <=1.0.0']

with open('README.rst') as file:
    long_description = file.read()

classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: System Administrators',
    'Intended Audience :: Information Technology',
    'Natural Language :: English',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
]

setup(
    name='pypuppetdb_daily_report',
    version=VERSION,
    author='Jason Antman',
    author_email='jason@jasonantman.com',
    packages=['pypuppetdb_daily_report', 'pypuppetdb_daily_report.tests'],
    entry_points="""
    [console_scripts]
    pypuppetdb_daily_report = pypuppetdb_daily_report
    """,
    url='http://github.com/jantman/pypuppetdb-daily-report/',
    license='Apache 2',
    description='Daily run summary report for PuppetDB, written in Python using nedap\'s pypuppetdb module.',
    long_description=long_description,
    install_requires=pyver_requires,
    keywords="puppet puppetdb report summary",
    classifiers=classifiers
)
