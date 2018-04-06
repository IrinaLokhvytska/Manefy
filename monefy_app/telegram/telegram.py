import telepot
from monefy_app import keys


class MonefyBot:
    key = keys.TRLEGRAM_KEY

    def test_bot(self):
        bot_account = telepot.Bot(self.key)
        return bot_account.getMe()


if __name__ == '__main__':
    bot = MonefyBot()
    print(bot.test_bot())
