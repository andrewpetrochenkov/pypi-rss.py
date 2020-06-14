# !/usr/bin/env python
import pypi_rss

for newest_package in pypi_rss.get_newest_packages():
    print(newest_package)
