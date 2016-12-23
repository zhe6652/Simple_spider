__author__ = 'Super.JZ'
import urllib.request

class HtmlDownloader():
    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)#可以拓展，添加头部等

        if response.getcode() != 200:
            return None
        return response.read()