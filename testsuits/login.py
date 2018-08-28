from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://v2.opgirl.cn/home?did=1&first=off")
time.sleep(6)
driver.refresh()
driver.maximize_window()
driver.implicitly_wait(6)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/header/div[1]/a").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/section[1]/input").send_keys(15600706692)
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/section[2]/div/input").send_keys(123456)
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/section[4]/input").click()
