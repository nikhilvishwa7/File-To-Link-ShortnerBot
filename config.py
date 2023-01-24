
import os


class config(object):
	API_ID = int(os.environ.get("API_ID", "6435225"))
	API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "5951446975:AAHomxCgmzt2HAyLF5K5E3nvoZGihYywY4Y")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "PyroStorageBot")
	CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001851293267"))
	SUPPORT_GROUP = os.environ.get("SUPPORT_CHAT", "TheDeadlyBots")
	SUPPORT_CHANNEL = os.environ.get("SUPPORT_CHANNEL", "TheBotUpdates")
        BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
        SHORTNER_SITE = os.environ.get("SHORTNER_SITE", "https://easysky.in")
        API_KEY = os.environ.get("API_KEY", "8644d61bb75d25519b6b0acdec99bf369fa1cbdd")
