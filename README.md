###功能   
* 爬取新浪微博信息：因为微博移动端的信息比PC端更容易爬取，所以本脚本是利用微博移动端爬取信息  [移动端微博url](weibo.cn)     

###输入   
* 用户id，从所需爬取用户的url中获得

###输出   
* 所有微博的评论数   
* 创建结果文件保存在G盘climberworm文件夹下，子文件夹名字为对应的用户id

###运行环境  
* 开发环境：python3.5  
* 第三方库：requests bs4

###使用说明
1.下载脚本   
   
    $ git clone https://github.com/shinytang6/weiboSpider.git
运行上述命令，将本项目下载到当前目录，如果下载成功当前目录会出现一个名为"weibospider"的文件夹；
2、用文本编辑器打开weibospider文件夹下的"weiboSpider.py"文件；
3、将"weiboSpider.py"文件中的“your cookie”替换成爬虫微博的cookie，后面会详细讲解如何获取cookie；
4、将"weiboSpider.py"文件中的user_id替换成想要爬取的微博的user_id，后面会详细讲解如何获取user_id；
