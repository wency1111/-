import requests
import re
from lxml import etree


html="https://www.23us.so/files/article/html/26/26336/index.html"
path=r'/mnt/hgfs/gx/project2/dingdianxiaoshuowang/article/ '
# for url in urls:
#     print(url)
def get_url(html):
    response = requests.get(html)
    response.encoding = "utf-8"
    text = response.text
    selector = etree.HTML(text)
    urls=re.findall(r'<td class="L">.*?<a href="(.*?)">',text,re.DOTALL)
    for url in urls:
        yield url


def get_content(url):
    h5=requests.get(url)
    h5.encoding="utf-8"
    text=h5.text
    selector=etree.HTML(text)
    titles=selector.xpath('// *[ @ id = "amain"] / dl / dd[1] / h1/text()')
    # print(path+titles[0])
    article_texts=selector.xpath('//*[@id="contents"]/text()')
    with open(path+titles[0],'w',encoding="utf-8")as f:
        for article_text in article_texts:
            f.write(article_text)

if __name__=="__main__":
    for url in get_url(html):
        get_content(url)
