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
    PHONE_PATH = ''
    MSG_PATH = ''
    sing_msg_multi_num(PHONE_PATH, MSG_PATH)
