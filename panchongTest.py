# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/04/15 20:46'
from bs4 import BeautifulSoup
info = []
with open("E:/BaiduNetdiskDownload/c0o3ao/html/org-list.html") as loginfile:
    soup =BeautifulSoup(loginfile,"lxml")
    images = soup.select("body > section > div > div.left > div.butler_list.company.list > div.layout > dl > dt > a > img")
    titles = soup.select("body > section > div > div.left > div.butler_list.company.list > div.layout > dl > dd > div > a > h1")
    cates = soup.select("body > section > div > div.left > div.butler_list.company.list > div.layout > dl > dd > ul > li.pic10 ")
    # print(repr(cate).decode("unicode–escape"))
    # print(images)

for image,title,cate in zip(images,titles,cates):
    date = {
        "image":image.get('data-url'),
        "title":title.get_text(),
        "cate":list(cate.stripped_strings)
    }
    info.append(date)
    # print repr(date).decode("unicode–escape")

temp =[ i for i in info if i["title"] ==u"北京大学" ]

print(repr(temp).decode("unicode–escape"))

