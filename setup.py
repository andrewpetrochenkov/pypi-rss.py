import setuptools

setuptools.setup(
    name='pypi-rss',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
