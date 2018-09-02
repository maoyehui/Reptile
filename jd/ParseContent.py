from bs4 import BeautifulSoup
from jd.DownloadUrl import download

def parse_jd(content):
    # 使用beautifulsoup解析html文档
    soup = BeautifulSoup(content)
    # 获取指定标签
    # tag_list = soup.find_all("div", "sku-name")
    tag_list = soup.find_all("span", "price J-p-2833305")
    for tag in tag_list:
        # 获取标签内容，并去除首尾空格
        print(tag)

    return None

if __name__ == '__main__':
    url = "https://item.jd.com/2833305.html"
    content = download(url)
    parse_jd(content)
