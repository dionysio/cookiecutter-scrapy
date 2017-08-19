# -*- coding: utf-8 -*-

"""
Scrape some sort of website...
"""

from scrapy.spiders import SitemapSpider


class {{cookiecutter.ClassName}}Spider(SitemapSpider):

    name = {{cookiecutter.project_name}}
    sitemap_urls = ['http://{{cookiecutter.domain}}/sitemap.xml']
    sitemap_rules = [
        ('/', 'parse'),
    ]
    start_urls = []

    def parse(self, response):
        pass
