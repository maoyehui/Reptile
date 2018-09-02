import urllib.request

# 下载网页，并设置重试次数
def download(url, num_retries=2):
    print('Downloading:', url)
    decode_list = ['utf-8', 'gbk', 'gb2312']
    content = None
    try:
        html = urllib.request.urlopen(url).read()
        for decode in decode_list:
            try:
                content = html.decode(decode)
                break
            except UnicodeDecodeError as e:
                continue
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
            return 'Download has faild!!!'
    return content

if __name__ == '__main__':
    html = download("https://search.bilibili.com/all?keyword=%E8%82%A1%E7%A5%A8&from_source=nav_search")
    # html = download("https://www.baidu.com")
    print(html)