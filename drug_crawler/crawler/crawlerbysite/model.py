from abc import *
import requests
from bs4 import BeautifulSoup
import sys, os
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))


class AbsCrawler(metaclass=ABCMeta):

    def __init__(self, url, service_keyword, service_key, order, parsing_keyword):
        self._url = url
        self._service_keyword = service_keyword
        self._service_key = service_key
        self._order = order
        self._parsing_keyword = parsing_keyword

    def _connect(self, keyword):
        keyword = str(keyword)
        if len(keyword) == 8:
            keyword = "0" + keyword
        print(keyword)
        api_url = self._url + self._service_keyword+self._service_key+self._order+keyword
        html = requests.get(api_url).text
        return html

    def _parsing(self, html):
        result = {}
        soup = BeautifulSoup(html, 'html.parser')
        for keyword in self._parsing_keyword:
            try:
                result[keyword] = soup.select(keyword)[0].text.strip()
            except:
                result[keyword] = -1
        return result

    def operating(self, keyword):
        html = self._connect(keyword=keyword)
        return self._parsing(html=html)


class PublicDataPortal(AbsCrawler):

    def __init__(self):
        AbsCrawler.__init__(self,'http://apis.data.go.kr/1471057/MdcinPrductPrmisnInfoService/getMdcinPrductItem?',
                            'ServiceKey=',
                            '77RgKiN2sETIeIDL1Fxb6%2BKmIwYHwJQGlmN5R7EWj2rUaOjQttyC43NM7YTyTZ4P9pjOqndDENRB1FNuFBWeew%3D%3D',
                            "&pageNo=1&numOfRows=100&bar_code=",
                            ['item_seq', 'item_name', 'entp_name', 'class_no', 'bar_code', 'material_name', 'edi_code', 'main_item_ingr','ingr_name', 'nb_doc_data'])