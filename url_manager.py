__author__ = 'Super.JZ'
class UrlManager():
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if not url:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if not urls or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def has_new_url(self):
       return len(self.new_urls) != 0