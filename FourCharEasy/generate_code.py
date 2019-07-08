from captcha.image import ImageCaptcha
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random

# 验证码中的字符,暂时不用汉子,使用字母,熟练之后可以尝试
number = list(map(str, range(10)))
uppercase_letter = list(map(chr, range(65, 91)))
lowercase_letter = list(map(chr, range(97, 123)))

# 验证码一般忽略大小写,长度为4个字符
def random_captcha_text(char_set=None, captcha_size=4) -> list:
    """
    随机生成长度为4的验证码
    :param char_set: 验证码字符串
    :param captcha_size: 默认为4
    :return: 验证码字符串列表
    """
    char_set = number + uppercase_letter + lowercase_letter if not char_set else char_set
    captcha_text = [random.choice(char_set) for _ in range(captcha_size)]
    return captcha_text

# 生成字符对应的验证码
def gen_captcha_text_and_image():
    image = ImageCaptcha()
    captcha_text = "".join(random_captcha_text())
    captcha = image.generate(captcha_text)
    # image.write(captcha_text, f"{captcha_text}.jpg")
    captcha_image = np.array(Image.open(captcha))
    return captcha_text, captcha_image



if __name__ == '__main__':
    text, image = gen_captcha_text_and_image()

    f = plt.figure()
    ax = f.add_subplot(111)
    ax.text(0.1, 0.9, text, ha='center', va='center', transform=ax.transAxes)
    plt.imshow(image)

    plt.show()
