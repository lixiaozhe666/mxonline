# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/04/16 21:15'
from bs4 import BeautifulSoup
import  requests

url ="https://my.qidian.com/bookcase"
header ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Cookie":"w7RePr18qXzxByPdIn0h7iQtII0AC4z8oPMIXioz; newstatisticUUID=1523878907_461154690; pgv_pvi=1195931648; pgv_si=s7728217088; e2=%7B%22pid%22%3A%22qd_P_qdlogin%22%2C%22eid%22%3A%22%22%7D; ywkey=ywHQbktbFwKc; ywguid=276855526; e1=%7B%22pid%22%3A%22qd_P_fin%22%2C%22eid%22%3A%22qd_A14%22%2C%22l1%22%3A2%7D"
}
wb_data = requests.get(url,headers=header)
soup =BeautifulSoup(wb_data.text,"lxml")


imgs = soup.select("#elRecList1 > li > a > img")
print(imgs)