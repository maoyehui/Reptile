import urllib.request
import re
from downloadUrl import download

# 使用正则匹配爬过滤后的网页
def link_crawler(seed_url, link_regex):
    """Crawl from the given seed URL following links matched by link_regex"""
    crawl_queue = [seed_url]
    while crawl_queue:
        # bytes to string
        url = crawl_queue.pop()
        # print(url)
        html = download(url)
        try:
            links = get_links(html.decode('utf-8'))
        except:
            links = get_links(html.decode('gb2312'))
        for link in links:
            print(">>>" + link)
            if re.match(link_regex, link):
                crawl_queue.append(link)

# 解析网页中<a>标签的
def get_links(html):
    """Return a list of links from html"""
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](http.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    res = webpage_regex.findall(html)
    return res

if __name__ == '__main__':
    html = "http://www.baidu.com"
    link_crawler(html, ".*com.*")