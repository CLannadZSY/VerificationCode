import random
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
智能无感知
        1. 安全用户
"""
class ClickVerify():

    def __init__(self):
        self.url = 'https://dun.163.com/trial/sense'
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument('--log info')
        chrome_options.add_argument('disable-infobars')
        self.browser = webdriver.Chrome(chrome_options=chrome_options, )
        # self.browser.maximize_window()

    def __del__(self):
        if self.browser:
            self.browser.close()

    def click_to_login(self):
        self.browser.get(self.url)
        time.sleep(5)

        for _ in range(3):
            ActionChains(self.browser).key_down(Keys.DOWN).perform()
            time.sleep(0.1)

        login_button = self.browser.find_element_by_xpath("//span[@class='yidun_intelli-text']")
        time.sleep(random.random() * 3)
        login_button.click()

        time.sleep(random.random() * 3)
        # text_present = EC.text_to_be_present_in_element((By.CLASS_NAME, 'yidun_classic-tips'), '验证成功')
        # print(text_present)
        # print(text_present(self.browser))
        try:
            element = WebDriverWait(self.browser, 10).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, 'yidun_classic-tips'), '验证成功')
            )
        except:
            print('error')


    def main(self):
        self.click_to_login()


if __name__ == '__main__':
    c = ClickVerify()
    c.main()
