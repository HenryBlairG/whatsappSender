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
def multi_msg_multi_num(file_path):
    wsp = Wsp(driver_path=os_join(getcwd(), 'chromedriver'))
    with open(file_path, 'r') as file_data:
        numb = ''
        msg = ''
        data = []
        for idx, line in enumerate(file_data):
            # print(f'\n\n{idx}  {line}\n\n')
            # number, msg = line.split(';')
            # print(f'{number}: {msg}')
            if not idx % 3:  # Es numero más intro
                numb, msg = line.split(';')
                msg = msg.replace('"', '')
                # print(f'{numb}, {msg}')
            elif idx % 3 == 1:
                msg += line
                # print(f'{numb}, {msg}')
            elif idx % 3 == 2:
                msg += line.replace('"', '')
                # print(f'{numb}, {msg}')
                data.append(s_url(numb, msg))
                numb, msg = '', ''
        wsp.pressEnter(data)


if __name__ == '__main__':
    from time import time
    t_start = time()
    # multi_msg_multi_num()
    total = time() - t_start
    if total < 60:
        print(f'Elapsed Time: {total}s')
    else:
        print(f'Elapsed Time: {total/60}m')
    