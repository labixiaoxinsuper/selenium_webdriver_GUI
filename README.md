基于selenium的webdriver包，通过chrome浏览器和Xpath Helper插件，对web GUI 进行自动化的操作。

web GUI操作需求：

a）对应的函数为initial_conditions()   
通过谷歌浏览器连接服务   
登录GUI   
![Image text](https://github.com/labixiaoxinsuper/selenium_webdriver_GUI/blob/master/img-folder/1.png)
 
b）对应的函数为add_domain()   
添加域名   
![Image text](https://github.com/labixiaoxinsuper/selenium_webdriver_GUI/blob/master/img-folder/2.png)    
![Image text](https://github.com/labixiaoxinsuper/selenium_webdriver_GUI/blob/master/img-folder/3.png)    
![Image text](https://github.com/labixiaoxinsuper/selenium_webdriver_GUI/blob/master/img-folder/4.png)     
当想要新建域名不存在的时候，那么点击“核对无误，确认提交”，就可以到“域名管理”的界面      
当添加的域名已经存在的时候，会出现下面的确定弹出框。所以由此来进行判断，如果有此“确定”按钮，那么域名已经存在。然后点击“返回按钮”     
![Image text](https://github.com/labixiaoxinsuper/selenium_webdriver_GUI/blob/master/img-folder/5.png) 
![Image text](https://github.com/labixiaoxinsuper/selenium_webdriver_GUI/blob/master/img-folder/6.png) 
![Image text](https://github.com/labixiaoxinsuper/selenium_webdriver_GUI/blob/master/img-folder/7.png)     

c）对应的函数为delete_domain()    
删除域名，因为要验证最多可以添加100个域名，所以无论想要新建的域名已经存在与否。都全部删除，为了方便下次使用。    

d）对应的函数为end_conditions()    
界面上退出   
断开服务，谷歌浏览器退出     
![Image text](https://github.com/labixiaoxinsuper/selenium_webdriver_GUI/blob/master/img-folder/8.png)     

运行步骤：    
在domain_operation.py更改如下信息，然后就可以直接运行了。    
![Image text](https://github.com/labixiaoxinsuper/selenium_webdriver_GUI/blob/master/img-folder/9.png) 

 




















