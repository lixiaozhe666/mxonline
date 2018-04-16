# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/04/16 19:39'
from bs4 import BeautifulSoup
import requests
import  time

# url ="https://www.qidian.com/finish"
urls = ["https://www.qidian.com/finish?action=hidden&orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=2&page={}".format(i+1) for i in range(20)]
def getCate(url,data=None):
    wb_data = requests.get(url)
    time.sleep(2)
    soup =BeautifulSoup(wb_data.text,"lxml")
    imgs =soup.select("div.book-img-box > a ")
    titles = soup .select("div.book-mid-info > h4 > a")
    marks = soup.select("div.book-mid-info > p.author > a[data-eid='qd_B60']")
    # print repr(marks).decode("unicode–escape")
    # print imgs
    for title,mark,img in zip(titles,marks,imgs):
        data = {
            "title":title.get_text(),
            "img":img.get("href"),
            "mark":mark.get_text()
        }

        print(repr(data).decode("unicode–escape"))

for url in urls:

    getCate(url)
