from setuptools import setup

setup(
    name='pypi-rss',
    version='2020.6.2',
    install_requires=[
        'requests_retry_on_exceptions',
        'setuptools',
        'xmltodict',
    ],
    packages=[
        'pypi_rss',
    ],
)
