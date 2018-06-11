import urllib.request

# 设置用户代理
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

html = download("http://www.baidu.com")

print(html)