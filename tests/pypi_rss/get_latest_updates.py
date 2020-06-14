# !/usr/bin/env python
import pypi_rss

for latest_update in pypi_rss.get_latest_updates():
    print(latest_update)
