from selenium import webdriver    #导入selenium框架
from selenium.webdriver.common.by import *  #导入selenium框架的包by方法包
from selenium.webdriver.edge.service import Service   #导入edge驱动包
from time import sleep   #导入时间休眠函数

driver=webdriver.Edge() #打开edge浏览器
driver.maximize_window()#浏览器最大化
driver.get("http://8.148.31.14:8081/phone_shop/admin/logout")#打开测试网站的url

driver.implicitly_wait(10)#隐式等待10秒
sleep(2)
driver.find_element(By.XPATH,"/html/body/div/form/div/div/div[2]/div[1]/input").send_keys("zhanlan")#输入账号
driver.find_element(By.XPATH,"/html/body/div/form/div/div/div[2]/div[2]/input").send_keys("123456")#输入账号
sleep(1)
driver.find_element(By.XPATH,"/html/body/div/form/div/div/div[2]/div[3]/button").click()#点击登录
sleep(3)
# driver.find_element(By.XPATH,"/html/body/div/div[2]/div/ul/li[1]/a").click()#1点击商品管理
# driver.find_element(By.LINK_TEXT,"商品管理").click()#2点击商品管理
driver.find_element(By.PARTIAL_LINK_TEXT,"商品管").click()#3.模糊
driver.find_element(By.XPATH,"/html/body/div/div[2]/div/ul/li[1]/dl/dd[2]/a").click()#点击添加商品
sleep(3)
iframe1=driver.find_element(By.XPATH,"/html/body/div/div[3]/iframe")#4.切入iframe框
#切出driver.switch_to.default_content()
# iframe1=driver.find_element(By.NAME,"myframe")#8.跟第四种写法任选一种
driver.switch_to.frame(iframe1)
driver.find_element(By.CSS_SELECTOR,"#goodsName").send_keys("iphon15")#5.输入商品名称
# driver.find_element(By.CLASS_NAME,"layui-input").send_keys("iphon15")#6.输入商品名称
# driver.find_element(By.ID,"goodsName").send_keys("iphon15")#7
driver.find_element(By.XPATH,"/html/body/div/form/div[2]/div/input").send_keys("6000")#输入商品价格
driver.find_element(By.XPATH,"/html/body/div/form/div[3]/div/input").send_keys("1")#输入商品库存

driver.find_element(By.XPATH,"/html/body/div/form/div[4]/div/div/div/input").click()#点击商品类别
driver.find_element(By.XPATH,"/html/body/div/form/div[4]/div/div/dl/dd[2]").click()#选择苹果手机
driver.find_element(By.XPATH,"/html/body/div/form/div[5]/div/div/div/input").click()#点击内存大小
driver.find_element(By.XPATH,"/html/body/div/form/div[5]/div/div/dl/dd[2]").click()#选择16GB

driver.find_element(By.XPATH,"/html/body/div/form/div[6]/div/input").send_keys("红色")#输入商品颜色红色
driver.find_element(By.XPATH,"/html/body/div/form/div[8]/div/textarea").send_keys("全新升级iphone15")#输入商品描述

driver.find_element(By.XPATH,"/html/body/div/form/div[9]/button[1]").click()#点击添加

input("按回车进行下一步，退出浏览器驱动")

#常见鼠标事件：
# 1.点击click()
# 2.清楚clear()
# 3.输入文本send_keys()
