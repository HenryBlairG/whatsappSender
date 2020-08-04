"""
Main File for Program
"""
from libs.url_utils import send_msg_url as s_url
from libs.wsp import WebWSP as Wsp
from os.path import join as os_join
from os import getcwd


def sing_msg_multi_num(numb_path,
                       msg_path):
    with open(numb_path) as numbers:
        with open(msg_path) as msg_chunks:
            msg = msg_chunks.readlines()
            m = "\n".join(msg)
            browser = Wsp(
                driver_path=os_join(
                    getcwd(),
                    'chromedriver'
                )
            )
            browser.pressEnter(
                [
                    s_url(
                        n,
                        m
                    ) for n in numbers
                ]
            )


if __name__ == '__main__':
    from random import shuffle
    from time import time
    # PHONE_PATH = ''
    # MSG_PATH = ''
    # sing_msg_multi_num(PHONE_PATH, MSG_PATH)
    data0 = [
        'https://web.whatsapp.com/send?phone=123&text=&source&data&app_absent'
        for _ in range(0)
    ]
    data1 = [
        'https://web.whatsapp.com/send?phone=56944361035&text={}&source&data&app_absent'.format(f'{i}'*(i+1))
        for i in range(200)
    ]
    # shuffle(data:= data0 + data1)
    data = data1[::-1]
    wsp = Wsp(driver_path=os_join(getcwd(), 'chromedriver'))
    t_start = time()
    wsp.pressEnter(pages=data)
    wsp.quit_driver()
    total = time() - t_start
    if total < 60:
        print(f'Elapsed Time: {total}s')
    else:
        print(f'Elapsed Time: {total/60}m')