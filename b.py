from f import *
from a import *
from c import *
from e import *

DB_URI = os.environ.get("DB_URI")
client = TelegramClient('ShortUrlLink', APP_ID, APP_HASH).start(
    bot_token=BOT_TOKEN)

