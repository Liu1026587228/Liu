import pytest
import allure
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver

@allure.feature("手机商城客户端测试报告")
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

    # 登录测试用例
    @allure.story("用户登录功能")
    @allure.title("用户正常登录用例")
    def test_login(self):
        self.do_login()
        sleep(2)
        # assert "zhanlan" in self.driver.page_source,"登录失败，右上角未显示用户名称"
        assert self.driver.title == "手机商城"
        assert self.driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/ul/li[1]/a").is_displayed(),"登录失败，未显示用户中心按钮"
        self.do_logout()
        sleep(3)

    #收藏测试用例
    @allure.story("用户商品收藏功能")
    @allure.title("用户收藏商品用例")
    def test_favorite(self):
        self.do_login()
        sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/ul/a[1]/li/img").click()  # 点击第一个商品
        sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/dl/dd[4]/button[1]").click()  # 点击收藏
        self.driver.refresh()#浏览器刷新
        sleep(3)
        assert self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/dl/dd[4]/button[2]").is_displayed(),"收藏失败，未显示取消收藏按钮"

    #取消收藏用例
    @allure.story("用户商品取消收藏功能")
    @allure.title("用户取消收藏商品用例")
    def test_least_favorite(self):
        self.do_login()
        sleep(4)
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[1]/a").click()  # 点击用户中心
        sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/ul/li[1]/a").click()  # 点击收藏中心
        sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div/ul/li/button[2]").click()  # 点击取消收藏
        sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/a[1]").click()  # 点击确定
        sleep(3)
        assert self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/ul/li[1]/a").is_displayed(), "收藏失败，未显示收藏中心"

    #下单用例
    @allure.story("用户正常下单功能")
    @allure.title("用户下单用例")
    def test_shop(self):
        self.do_login()
        sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/ul/a[1]/li/img").click()  # 点击第一个商品
        sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/dl/dt[4]/button").click()  # 点击加入购物车
        sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/dl/dd[4]/button[3]").click()  # 点击去购物车
        sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/form/table/tbody/tr[2]/td[1]/div/label/input").click()  # 点击是否购买
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[2]/button").click()  # 点击确认购买
        sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[1]/label/input").click()  # 点击第一个收货地址
        sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[3]/button").click()  # 点击确认下单
        sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/button[2]").click()  # 点击立即支付
        sleep(3)
        assert self.driver.find_element(By.XPATH,"/html/body/div[1]/div/button[2]").is_displayed(),"下单失败，未显示查看订单"

