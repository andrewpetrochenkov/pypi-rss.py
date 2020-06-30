<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/pypi-rss.svg?maxAge=3600)](https://pypi.org/project/pypi-rss/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/pypi-rss.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/pypi-rss.py/actions)

### Installation
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
    print(p['pubdate'], p['name'], p['description'])

for p in pypi_rss.get_latest_updates():
    print(p['pubdate'], p['name'], p['version'], p['description'])
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>