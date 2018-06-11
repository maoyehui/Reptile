import urllib.request
import re

def download(url, user_agent='wswp', num_retries=2):
    print('Downloading:', url)

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', user_agent)]
    try:
        html = opener.open(url).read()
    except urllib.request.URLError as e:
        print('Download error:', e.reason)
        html = None
        i = 1
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                print('Retry '+ i.__str__() +'times')
                i += 1
                return download(url, num_retries-1)
        else:
            return 'Download have faild!!!'
    return html

# 网站地图爬虫
def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url).decode('utf-8')
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    print('link:' + links.__str__())
    for link in links:
        html = download(link)
        print(html)

if __name__ == '__main__':
    crawl_sitemap("http://example.webscraping.com/sitemap.xml")