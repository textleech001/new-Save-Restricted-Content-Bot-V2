# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "27392387"))
API_HASH = getenv("API_HASH", "37ee47c18c8be62716a27335a771e7da")
BOT_TOKEN = getenv("BOT_TOKEN", "7790663224:AAEP4TdtMohfq-wPrYXJaCC2rfl33OUMf3k")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5787359348").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Bhardwaj:7vVHr6zrvpsMsU3@cluster0.p2smf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002406770624")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002197825290"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "5"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "nanoshare.in")
AD_API = getenv("AD_API", "9d3a07e557623ce75d4f1639359a64e3d270d30d")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
