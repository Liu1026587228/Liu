from selenium import webdriver    #导入selenium框架
from selenium.webdriver.common.by import *  #导入selenium框架的包by方法包
from selenium.webdriver.edge.service import Service   #导入edge驱动包
from time import sleep   #导入时间休眠函数

driver=webdriver.Edge() #打开edge浏览器
driver.maximize_window()#浏览器最大化
driver.get("http://sealong.yyboxdns.com:13811/phone_shop/view/index")#打开测试网站的url

driver.implicitly_wait(10)#隐式等待10秒
sleep(2)
driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/ul/li[1]/a").click()#点击注册
driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div/div[2]/div[1]/input").send_keys("aaa")#输入昵称
driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div/div[2]/div[2]/input").send_keys("123456")#输入密码
driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div/div[2]/div[3]/input").send_keys("123456")#输入确认密码
driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div/div[2]/div[4]/input").send_keys("15513134646")#输入手机号
driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div/div[2]/div[5]/input").send_keys("1026@qq.com")#输入邮箱
driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div/div[2]/div[6]/button").click()#点击注册
sleep(3)
driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div/div[2]/div[1]/input").send_keys("aaa")#输入用户名
driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div/div[2]/div[2]/input").send_keys("123456")#输入密码
driver.find_element(By.XPATH,"/html/body/div[1]/form/div/div/div[2]/div[3]/button").click()#点击注册

input("按回车进行下一步，退出浏览器驱动")

#常见鼠标事件：
# 1.点击click()
# 2.清楚clear()
# 3.输入文本send_keys()
