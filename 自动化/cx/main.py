from selenium import webdriver
import time

chromeDriver = webdriver.Chrome(executable_path="E:\\python\\chromedriver.exe")

chromeDriver.get("E:\\笔记\\笔记\\day1联系\\跳转页面\\pop.html")

chromeDriver.maximize_window()

chromeDriver.find_element_by_link_text("click me").click()

chromeDriver.switch_to.window(chromeDriver.window_handles[1])

chromeDriver.find_element_by_id("kw").send_keys("java")

chromeDriver.find_element_by_id("su").click()

time.sleep(3)

chromeDriver.quit()
