'''
Colors for messages:
White - information, actions, user input
Green - postitive messages
Red - negative messages
Yellow - errors
Cyan - Card intro info
'''


class Logger():
    def __init__(self):
        self.msg_log = []

    def show_msg(self, msg):
        print(msg)
        self.msg_log.append(msg)

    def show_gain(self, msg):
        print(msg)
        self.msg_log.append(msg)

    def show_loss(self, msg):
        print(msg)
        self.msg_log.append(msg)

    def show_warning(self, msg):
        print(msg)
        self.msg_log.append(msg)

    def show_card(self, msg):
        print(msg)
        self.msg_log.append(msg)
