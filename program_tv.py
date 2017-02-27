import re
import string
import sys
import os
import urllib

from bs4 import BeautifulSoup
import requests
from lxml import etree

user_id=5350703203
#user_id=1669879400
cookie={"Cookie":"_T_WM=2e99e343902a268f5241aeb10504512a; SUB=_2A251t_0PDeRxGeNG4lQV8yrIzzyIHXVXW4NHrDV6PUJbkdBeLWHhkW0WF57bbK-sFn8vDu7RsmM8dM2hxg..; SUHB=0N21gwftxxwTPR; SCF=AskWEwn80EfAaqg9x9E_jjwTaXGfYFZ2XFI-6-0s5LKRBngQAn_i8TE1EVRjkINfdnal7Nq9HWq_52ArdpkzeW4.; SSOLoginState=1488162143; H5_INDEX=2"}
pages=30
for page in range(pages):
  url = 'http://weibo.cn/u/%d?page=%d&filter=0'%(user_id,page)
  path=str(user_id)
  os.makedirs(os.path.join("G:\climberworm", path)) ##创建一个存放套图的文件夹
  os.chdir("G:\climberworm\\"+path) ##切换到上面创建的文件夹
  # url ='http://weibo.com/p/10080887f2e6485dd785d69d9a16a6edaf1ce6?page=%d'%(page)
  html = requests.get(url,cookies=cookie)
   
  Soup = BeautifulSoup(html.text, 'lxml')

  alla=Soup.find_all("div",class_="c")    #所有的微博
  for a in alla:
     per = a.find("a",class_="cc")  #每条微博的评论
     regular1=re.compile(r"\d+")
     pgs = regular1.findall(per.text)  #每条微博对应的评论数
    
     href=per['href']  #每条微博对应的评论链接
     comments = requests.get(href,cookies=cookie)
     soup = BeautifulSoup(comments.text, 'lxml')
     comment = soup.find_all("div",class_="c")#评论链接里评论的div


     for cmt in comment:
       
       content = cmt.find("span",class_="ctt")   #评论内容
      
       time = cmt.find("span",class_="ct")
       if (content):
           name="comment"
           f = open(name+'.txt', 'a+',encoding="utf-8")
           f.write(time.text[:19]+"     "+content.text+"\n")
          #print(content.text,time.text[:19])
      
     if(int(pgs[0])>10):              #一条微博的评论数大于10，即有多页
        regular2=re.compile(r"\d+")
        pg=soup.find("div",class_="pa").find("div")   
        
        pagenum=regular2.findall(pg.text)[1]   #抓取页数
        for i in range(2,int(pagenum)+1):       
           newhref=per['href'][:-7]+"&page=%d"%(i)    #第i页的url
           newcomments = requests.get(newhref,cookies=cookie)
           newsoup = BeautifulSoup(newcomments.text, 'lxml')
           newcomment = newsoup.find_all("div",class_="c")           
 
           for newcmt in newcomment:
       
              newcontent = newcmt.find("span",class_="ctt") 
              
              newtime = newcmt.find("span",class_="ct")
              if (newcontent):
                name="comment"
                f = open(name+'.txt', 'a+',encoding="utf-8")
                f.write(newtime.text[:19]+"     "+newcontent.text+"\n")
         
   
