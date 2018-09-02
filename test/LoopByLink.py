import re
from test.downloadUrl import download

# 使用正则匹配爬过滤后的网页
def link_crawler(seed_url, link_regex):
    """Crawl from the given seed URL following links matched by link_regex"""
    # default decode queue
    decode_list = ['utf-8', 'gb2312', 'gbk']
    crawl_queue = [seed_url]
    # keep track which URL's have been seen before
    seen = set(crawl_queue)
    while crawl_queue:
        # bytes to string
        url = crawl_queue.pop()
        # print(url)
        html = download(url)
        for decode in decode_list:
            # 对下载的网页代码解析编码
            try:
                links = get_links(html.decode(decode))
                for link in links:
                    print(">>>" + link)
                if re.match(link_regex, link):
                    # check if have already seen this link
                    if link not in seen:
                        seen.add(link)
                        crawl_queue.append(link)
            # 编码解析异常，使用其他编码解析
            except:
                continue


# 解析网页中<a>标签的
def get_links(html):
    """Return a list of links from html"""
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](http.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    res = webpage_regex.findall(html)
    return res

if __name__ == '__main__':
    # html = "http://www.baidu.com"
    html = "https://item.jd.com/2833305.html"
    link_crawler(html, ".*com.*")
