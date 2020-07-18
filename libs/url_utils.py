from urllib.parse import quote


START_CHAT = 'https://web.whatsapp.com/send?phone={0}&text={1}&source&data&app_absent'


def no_msg_url(phone_number=None):
    return START_CHAT.format(phone_number, '')


def send_msg_url(phone_number=None, message=None):
    return START_CHAT.format(phone_number, quote(message))


def send_msgs(file_stream):
    '''
    create a generator of urls ready  to send.
    :param file_stream: File with number and message on every line
    :return: generator
    '''
    yield


if __name__ == '__main__':

    pass
 #    NUM_PROB = '56944361035'
 #    MSG_PROB = '''Kenneth G. Johnston once wrote as follows. A story, but always anecdotes, sketches, contests and so on. "Johnston The topic is a very useful tool for the future.
 #
 # Questions about Sears Hemingway's white elephant: Hill like white elephant / Ernest Hemingway 1. What are they talking about? (Evidence ...) Men and girls are talking about abortion. Evidence: "White Elephant" ~ A white elephant is sacred in some countries, but usually a white elephant is not considered a good thing ... The idea is really good to have a white elephant, but once Obviously, you get it, it does not have real value and needs to be maintained a lot. In addition, Indian rulers often send white elephants to those who hate B / C, and this person will be economically destroyed. Please observe this value.
 #
 # Author "Like an
 #    '''
 #    print(send_msg_url(NUM_PROB, MSG_PROB))
