import abc


class AbstractDataStore(object):
    @abc.abstractmethod
    def store_data(self, data):
        pass


class AbstractParser(object):
    @abc.abstractmethod
    def parser(self, page_url, html_cont):
        pass

    @abc.abstractmethod
    def _get_new_urls(self, page_url, soup):
        pass

    @abc.abstractmethod
    def _get_data(self, page_url, soup):
        pass
