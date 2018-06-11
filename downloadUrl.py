import urllib.request

# 下载网页，并设置重试次数
def download(url, num_retries=2):
    print('Downloading:', url)
    try:
        html = urllib.request.urlopen(url).read()
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

# if __name__ == '__main__':
#     html = download("http://www.meetup.com")
#     print(bytes.decode(html))