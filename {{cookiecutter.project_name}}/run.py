#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from scrapy import cmdline

if __name__ == '__main__':
    cmdline.execute(["scrapy", "crawl", '{{cookiecutter.project_name}}'] + sys.argv[1:])
