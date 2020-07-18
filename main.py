"""
Main File for Program
"""
# from libs.url_utils import send_msg_url as s_url
from libs.wsp import WebWSPHandler as Wsp
from os.path import join as os_join
from os import getcwd


if __name__ == '__main__':
    browser = Wsp(driver_path=os_join(getcwd(), 'chromedriver'))
    browser.pressEnter([])
