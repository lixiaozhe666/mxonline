# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/04/17 20:04'
from bs4 import BeautifulSoup
import  requests
import  time
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sArticle =""
urlcontent ="https://m.qidian.com/book/{}/{}".format("1003782761","321319656")
url = "https://m.qidian.com/majax/chapter/getChapterInfo?_csrfToken=w7RePr18qXzxByPdIn0h7iQtII0AC4z8oPMIXioz&bookId={}&chapterId={}".format("1003782761","321319656")
f = open('C:\Users\Administrator\Desktop\\test.txt', 'w')


def xiaoshuo(url,urlcontent,sArticle):
    wb_data = requests.get(url)
    soup =BeautifulSoup(wb_data.text,'lxml')
    wb_Content = requests.get(urlcontent)
    soupContent =BeautifulSoup(wb_Content.text,'lxml')
    title = soupContent.select("#chapterContent > section > h3")
    article = soupContent.select("#chapterContent > section > p")
    print title[0].get_text()
    f.writelines(str(title[0].get_text()) + "\n")
    for p in article:
        sArticle +=p.get_text()
        f.writelines(str(p.get_text())+"\n")

    print sArticle
    jsonStr = json.loads(soup.text)

    nextCharId=jsonStr["data"]["chapterInfo"]["next"]
    print(nextCharId)
    return nextCharId

for i in range(5):
    nextId = xiaoshuo(url, urlcontent, sArticle)
    urlcontent = "https://m.qidian.com/book/{}/{}".format("1003782761", nextId)
    url = "https://m.qidian.com/majax/chapter/getChapterInfo?_csrfToken=w7RePr18qXzxByPdIn0h7iQtII0AC4z8oPMIXioz&bookId={}&chapterId={}".format("1003782761", nextId)
    sArticle =""
f.close()