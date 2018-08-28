import unittest
from selenium import webdriver
import time


class Login_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def login(self, phonenum, password):
        self.driver.get("https://v2.opgirl.cn/home?did=1&first=off")
        time.sleep(6)
        self.driver.refresh()
        self.driver.implicitly_wait(6)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/header/div[1]/a").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/section[1]/input").send_keys(phonenum)
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/section[2]/div/input").send_keys(
            password)
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/section[4]/input").click()

    def test_login_success(self):
        '''  登陆成功'''
        self.login("15600706692", "123456")
        time.sleep(2)

    def test_login_pwd_error(self):
        '''用户名正确，密码错误'''
        self.login('15600706692', '1111111')
        time.sleep(1)
        error_message = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/section[3]/span').text
        self.assertIn("手机号密码错误", error_message)

    def tearDown(self):
        time.sleep(2)
        print("test over !!!")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
