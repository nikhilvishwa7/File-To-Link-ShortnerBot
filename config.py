
import os


class config(object):
	API_ID = int(os.environ.get("API_ID", "21748181"))
	API_HASH = os.environ.get("API_HASH", "b1d962414e186e0778911f3183feac33")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6194259486:AAHleGiC0sq9pV8XHGtoa41RlsulFCTKLGI")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "Rename_4GB_bot")
	CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001932233757"))
	SUPPORT_GROUP = os.environ.get("SUPPORT_CHAT", "NewMovie1stOnTG")
	SUPPORT_CHANNEL = os.environ.get("SUPPORT_CHANNEL", "bot_channel_011")
        BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
        SHORTNER_SITE = os.environ.get("SHORTNER_SITE", "https://TinyFy.in")
        API_KEY = os.environ.get("API_KEY", "8f29e4130ed3439c4c5cfc5c56dae86c0aff0daa")
