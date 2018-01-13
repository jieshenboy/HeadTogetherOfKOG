# HeadTogetherOfKOG
王者荣耀英雄头像拼接
![Aaron Swartz](/com/showData/HeadTogether.jpg)
##项目结果如图上所示
##项目环境
####python3.x
##使用方法
  可以点击项目中的com/main.py文件，即可自动执行
##项目说明
###图片来源
通过浏览王者荣耀游戏官网英雄资料，网址为http://pvp.qq.com/web201605/herolist.shtml
打开浏览器开发者工具（浏览器控制台），可以看到有一串JavaScript脚本
![Aaron Swartz](raw.githubusercontent.com/jieshenboy/HeadTogetherOfKOG/master/com/showData/WebCodejs.png)
从图中我们可以看到有一个json文件，此文件保存了英雄列表的名称，我们可以通过它来查找图片。
我们观察头像图片对应的URL可知，例如：http://game.gtimg.cn/images/yxzj/img201606/heroimg/501/501.jpg
最后的501对应的就是json里面的英雄编号，所以可以通过这个URL规律将图片下载下来并进行拼接。
