import itchat


class WeChat(object):

    __ITCHAT__ = None

    def login(self):
        itchat.auto_login()
        WeChat.__ITCHAT__ = itchat
        return True

    def getUserName(self):
        if WeChat.__ITCHAT__ == None:
            WeChat.login(self)

        nickName = input('请输入好友微信昵称:')
        UserName = WeChat.__ITCHAT__.search_friends(name=nickName.strip())
        while len(UserName) == 0:
            print('该昵称好友不存在，请重新输入')
            nickName = input('请输入好友微信昵称:')
            UserName = WeChat.__ITCHAT__.search_friends(name=nickName.strip())
        return UserName[0]['UserName']

    def sendMessage(self,message,userName):
        if message == '':
            return False
        if WeChat.__ITCHAT__ == None:
            WeChat.login(self)

        WeChat.__ITCHAT__.send(message,toUserName=userName)
        return True


