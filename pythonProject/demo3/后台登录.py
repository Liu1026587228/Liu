from selenium import webdriver    #导入selenium框架
from selenium.webdriver.common.by import *  #导入selenium框架的包by方法包
from selenium.webdriver.edge.service import Service   #导入edge驱动包
from time import sleep   #导入时间休眠函数

driver=webdriver.Edge() #打开edge浏览器
driver.maximize_window()#浏览器最大化
driver.get("http://sealong.yyboxdns.com:13811/phone_shop/admin/logout")#打开测试网站的url

driver.implicitly_wait(10)#隐式等待10秒
sleep(2)
driver.find_element(By.XPATH,"/html/body/div/form/div/div/div[2]/div[1]/input").send_keys("zhanlan")#输入账号
driver.find_element(By.XPATH,"/html/body/div/form/div/div/div[2]/div[2]/input").send_keys("123456")#输入账号
driver.find_element(By.XPATH,"/html/body/div/form/div/div/div[2]/div[3]/button").click()#点击登录


input("按回车进行下一步，退出浏览器驱动")

#常见鼠标事件：
# 1.点击click()
# 2.清楚clear()
# 3.输入文本send_keys()
