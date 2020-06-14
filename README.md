<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/v/pypi-rss.svg?maxAge=3600)](https://pypi.org/project/pypi-rss/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![Travis](https://api.travis-ci.org/andrewp-as-is/pypi-rss.py.svg?branch=master)](https://travis-ci.org/andrewp-as-is/pypi-rss.py/)

#### Installation
```bash
$ [sudo] pip install pypi-rss
```

#### Pros
Batteries included:
+   xml and datetime parser
+   requests/xml exceptions catch. ready for production usage! :)

#### Examples
```python
import pypi_rss

for p in pypi_rss.get_newest_packages():
    print(p['title'], p['pubdate'], p['name'])

for p in pypi_rss.get_latest_updates():
    print(p['title'], p['pubdate'], p['name'], p['version'])
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>