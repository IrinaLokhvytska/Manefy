import telepot
import keys
from telepot.loop import MessageLoop


class MonefyBot:
    bot_account = telepot.Bot(keys.TRLEGRAM_KEY)

    def test_bot(self):
        return self.bot_account.getMe()

    def handle(self, msg):
        chat_id = msg['chat']['id']
        self.bot_account.sendMessage(chat_id, msg['text'])


if __name__ == '__main__':
    bot = MonefyBot()
    MessageLoop(bot.bot_account, bot.handle).run_as_thread()
    print(bot.test_bot())
