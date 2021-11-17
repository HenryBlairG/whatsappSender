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
def multi_msg_multi_num(number_path, msg_path):
    wsp = Wsp(driver_path=os_join(getcwd(), 'chromedriver'))
    with open(number_path) as numbers:
        with open(msg_path) as messages:
            data = list(map(lambda x: s_url(x[0], x[1]), zip([n.strip() for n in numbers], messages.read().split(';'))))
            # print(data)
            wsp.pressEnter(data)


if __name__ == '__main__':
    from time import time
    t_start = time()
    multi_msg_multi_num('tmp/fonos.txt', 'tmp/mensajes.txt')
    total = time() - t_start
    if total < 60:
        print(f'Elapsed Time: {total}s')
    else:
        print(f'Elapsed Time: {total/60}m')
    