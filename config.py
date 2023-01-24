
import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-100"))
	SUPPORT_GROUP = os.environ.get("UPDATES_CHANNEL", "")
	SUPPORT_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
        BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
        SHORTNER_SITE = os.environ.get("SHORTNER_SITE", "")
        API_KEY = os.environ.get("API_KEY", "")
