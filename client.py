#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

from bs4 import BeautifulSoup


class BotClient(object):

    def get_http_response(self):
        http_response = urllib2.urlopen("https://www.packtpub.com/packt/offers/free-learning/")
        response_readed = http_response.read()
        http_response.close()
        return response_readed

    def get_book_name(self, body):
        bs = BeautifulSoup(body)
        dotd_title_div = bs.find("div", "dotd-title")
        book_name = dotd_title_div.find("h2")
        book_name_processed = str(book_name).split()
        book_name_processed = book_name_processed[1:len(book_name_processed) - 1]
        return " ".join(book_name_processed)
