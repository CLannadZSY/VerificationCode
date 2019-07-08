import time
import random
import re
from PIL import Image
from PIL import ImageGrab
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

USERNAME = '123'
PASSWORD = '123'


class Bilibili():
    def __init__(self):
        self.url = 'https://passport.bilibili.com/login'
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument('--log info')
        chrome_options.add_argument('disable-infobars')
        self.browser = webdriver.Chrome(chrome_options=chrome_options,)
        self.browser.maximize_window()
        self.email = USERNAME
        self.password = PASSWORD

    def __del__(self):
        """析构函数"""

        pass

    def login(self):
        self.browser.get(self.url)
        time.sleep(5)
        self.browser.find_element_by_id('login-username').send_keys(self.email)
        time.sleep(random.random() * 3)
        self.browser.find_element_by_id('login-passwd').send_keys(self.password)
        time.sleep(random.random() * 3)
        # 截取验证图片1
        # image = ImageGrab.grab()
        # slider = self.browser.find_element_by_class_name('gt_slider_knob')
        # ActionChains(self.browser).release(slider).perform()
        # time.sleep(1)
        # self.browser.save_screenshot('big.png')  # 只是截图浏览器窗口内容
        # img1 = Image.open('big.png')
        # img1 = img1.crop((983, 210, 1273, 370))  # (left, top, left+width, top+height)这几个数值表示
        # img1.save('1.png')
        # image1 = Image.open('1.png')
        # image1_array = image1.load()
        login_button = self.browser.find_element_by_xpath("//li[@class='btn-box']/a[1]")
        login_button.click()
        # 后面换成,等待验证码加载完成再往下执行
        # https://blog.csdn.net/u013250071/article/details/79133116
        time.sleep(5)

        verify_img = self.browser.find_element_by_xpath("//canvas[@class='geetest_canvas_slice geetest_absolute']")
        verify_img_left_top = verify_img.location
        verify_img_size = verify_img.size
        print(verify_img_left_top, verify_img_size)
        time.sleep(3)


        self.browser.save_screenshot('big.png')  # 只是截图浏览器窗口内容
        img1 = Image.open('big.png')
        # (left, top, left+width, top+height)这几个数值表示
        img1 = img1.crop((verify_img_left_top['x'], verify_img_left_top['y'],
                          verify_img_left_top['x'] + verify_img_size['width'],
                          verify_img_left_top['y'] + verify_img_size['height']))

        print((verify_img_left_top['x'], verify_img_left_top['y'],
                          verify_img_left_top['x'] + verify_img_size['width'],
                          verify_img_left_top['y'] + verify_img_size['height']))
        # (1107, 320) (1423,515)
        img1.save('1.png')
        # image1 = Image.open('1.png')
        # image1_array = image1.load()

        # 截取验证图片2
        # ActionChains(self.browser).click_and_hold(slider).perform()
        # # screenshot_2 = self.browser.get_screenshot_as_png()
        # time.sleep(1)
        # self.browser.save_screenshot('big2.png')
        # img2 = Image.open('big2.png')
        # img2 = img2.crop((983, 210, 1273, 370))
        # img2.save('2.png')
        # image2 = Image.open('2.png')
        # image2_array = image2.load()
        # # 判断需要滑动的距离
        # # 滑动的部分与阴影部分的差值大概在60以上80以下，因此采用如下判断
        # # 0,1,2是分别对应rgb色值
        # # 截图下来大小290*160，下面数值范围选择考虑到排除其他影响因素就只留滑块阴影部分
        # for i in range(70, 270):
        #     for j in range(20, 100):
        #         if image1_array[i, j][0] - image2_array[i, j][0] > 60 and image1_array[i, j][1] - image2_array[i, j][
        #             1] > 60 and image1_array[i, j][2] - image2_array[i, j][2] > 60:
        #             border = i
        # print(border)
        # # 构造滑动列表
        # track = []
        # current = 0
        # # 其实64这个值大概准确有时出错，因为他滑块其实位置可能会有偏差，所以下面重新调用多次尝试
        # while current < border - 64:
        #     track.append(1)
        #     current += 1
        # print(track)
        # # 滑动滑块
        # # 直接匀速滑动肯定通不过，先加速后减速效果也不是很好。
        # # 但是这种简单的方法，每移动一次随机停顿0-1秒之间骗过了极验，通过率很高
        # # click_and_hold 点击不放，move_by_offset 按坐标移动，release 鼠标释放
        # ActionChains(self.browser).click_and_hold(slider).perform()
        # for x in track:
        #     ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        #     time.sleep(random.random() / 100)
        # time.sleep(random.random())
        # ActionChains(self.browser).release().perform()
        # time.sleep(5)
        #
        # rsp = self.browser.page_source
        #
        # # 已登录的页面有‘大会员’菜单栏，未登录页面没有，
        # # 所以用正则判断以下。 如果正则未匹配到，证明登录失败，尝试再次登录
        # if re.findall(r'大会员', rsp, re.S):
        #     print('Login successfully ...')
        # else:
        #     print('Try again ...')
        #     self.login()

        self.browser.quit()

if __name__ == '__main__':
    b = Bilibili()
    b.login()
