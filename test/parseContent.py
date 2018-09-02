from bs4 import BeautifulSoup
from test.downloadUrl import download

def parse(content):
    soup = BeautifulSoup(content)
    tag_list = soup.find_all("div", "sku-name")
    for tag in tag_list:
        print(tag.string.strip())
    return None

if __name__ == '__main__':
    url = "https://item.jd.com/2833305.html"
    content = download(url).decode("gbk")
    parse(content)