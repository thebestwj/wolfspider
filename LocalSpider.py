from URLManager import UrlManager
from Downloader import HtmlDownloader
from BikeParser import BikeParser
from SimpleHtmlDataStore import SimpleHtmlDataStore
import time


class Spider(object):
    def __init__(self):
        self.urlManager = UrlManager()
        self.downloader = HtmlDownloader()
        self.dataStore = SimpleHtmlDataStore()
        self.parser = BikeParser()

    def start(self, url):

        if self.urlManager.has_new_url():
            url = self.urlManager.get_new_url()

        for _ in range(20):
            urls = []
            data = {}
            print('now crawling: %s' % url)
            cont = self.downloader.download(url)
            urls, data = self.parser.parser(url, cont)
            if urls is not None:
                self.urlManager.add_new_urls(urls)
            print('have %d urls to go' % self.urlManager.new_url_size())
            if data is not None:
                self.dataStore.store_data(data)
            if self.urlManager.has_new_url():
                url = self.urlManager.get_new_url()
            time.sleep(1)
        self.urlManager.save()


if __name__ == '__main__':
    spider = Spider()
    url = 'https://baike.baidu.com/view/681007'
    spider.start(url)
