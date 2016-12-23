__author__ = 'Super.JZ'
from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser():
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href = re.compile(r"/view/\d+\.htm"))#可以加一个get——ext——links方法
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data={}
        res_data['url'] = page_url
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data["title"] = title_node.get_text()

        summary_node = soup.find('div', class_="para")
        res_data["summary"] = summary_node.get_text()
        return res_data

    def parse(self, page_url, html_cont):
        if not page_url or not html_cont:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding="gb18030")
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data