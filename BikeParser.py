import re
from bs4 import BeautifulSoup

from AbstractClasses import AbstractParser


class BikeParser(AbstractParser):
    def parser(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_data(page_url,soup)
        return new_urls,new_data

    def _get_new_urls(self,page_url,soup):
        """
        获取爬取的链接
        :param page_url:
        :param soup:
        :return:
        """
        new_urls = set()
        links = soup.find_all('a',href = re.compile(r'/item/.+'))
        for link in links:
            new_url = 'https://baike.baidu.com' + link['href']
            new_urls.add(new_url)
        return new_urls

    def _get_data(self,page_url,soup):
        """
        主解析器
        :param page_url:
        :param soup:
        :return:
        """
        data = {}
        data['url'] = page_url
        title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        summary = soup.find('div',class_='lemma-summary')
        if title is None or summary is None:
            return None
        data['title'] = title.get_text()
        data['summary'] = summary.get_text()
        return data