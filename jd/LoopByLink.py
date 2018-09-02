import re
from jd.DownloadUrl import download

# 使用正则匹配爬过滤后的网页
def link_crawler(seed_url, link_regex):
    """Crawl from the given seed URL following links matched by link_regex"""
    crawl_queue = [seed_url]
    # keep track which URL's have been seen before
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)

        links = get_links(html)
        for link in links:

            # if re.match(link_regex, link):
            #     # check if have already seen this link
            #     if link not in seen:
            #         seen.add(link)
            #         # crawl_queue.append(link)
            if link[-3:] == "css":
                print(link)





# 解析网页中<a>标签的
def get_links(html):
    """Return a list of links from html"""
    # a regular expression to extract all links from the webpage
    # webpage_regex = re.compile('<a[^>]+href=["\'](http.*?)["\']', re.IGNORECASE)
    webpage_regex = re.compile('<link[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    res = webpage_regex.findall(html)
    return res

if __name__ == '__main__':
    # html = "http://www.baidu.com"
    html = "https://item.jd.com/2833305.html"
    link_crawler(html, ".*com.*")
