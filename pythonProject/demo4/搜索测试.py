import pytest
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver


class Testphone_shop():
    def setup_method(self, method):  # 每个测试用例运行时，首先执行的方法
        self.driver = webdriver.Edge()  # 调用浏览器
        self.vars = {}

    def teardown_method(self, method):  # 每个测试用例运行结束后，执行的方法
        self.driver.quit()  # 退出浏览器

    def do_login(self):
        self.driver.get("http://8.148.31.14:8081/phone_shop/view/index")
        self.driver.implicitly_wait(10)  # 隐式等待10秒
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/a").click()  # 点击登录
        sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/form/div/div/div[2]/div[1]/input").send_keys(
            "zhanlan")  # 输入账号
        self.driver.find_element(By.XPATH, "/html/body/div[1]/form/div/div/div[2]/div[2]/input").send_keys(
            "123456")  # 输入账号
        self.driver.find_element(By.XPATH, "/html/body/div[1]/form/div/div/div[2]/div[3]/button").click()  # 点击登录

    def do_logout(self):
        self.driver.find_element(By.CSS_SELECTOR, ".caret").click()
        self.driver.find_element(By.LINK_TEXT, "注销登录").click()

    #搜索测试
    def test_search(self):
        self.do_login()
        sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/div/form/div/input").send_keys("iphone")  # 输入iphone
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/div/form/button").click()  # 点击查找
        sleep(3)