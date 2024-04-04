
import os


class config(object):
	API_ID = int(os.environ.get("API_ID", "21748181"))
	API_HASH = os.environ.get("API_HASH", "b1d962414e186e0778911f3183feac33")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6307039266:AAGpIhJ6xgGFEV6X7W6miVHb0TdaYnX4USU")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "TestCorner07Bot")
	CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001537820228"))
	SUPPORT_GROUP = os.environ.get("SUPPORT_CHAT", "Spiderman_No_Way_home77")
	SUPPORT_CHANNEL = os.environ.get("SUPPORT_CHANNEL", "Spiderman_No_Way_home77")
        BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", '5149183428')).split()
        SHORTNER_SITE = os.environ.get("SHORTNER_SITE", "https://Omnifly.in.net")
        API_KEY = os.environ.get("API_KEY", "45c911f1b1d6c57c9b01b64ec7780416591e5903")
