# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "26948104"))
API_HASH = getenv("API_HASH", "5cd7c8dbc4331f9db28e83c25b8fe12e")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5971647539").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://aaradhyverma256:8CR1AaSBP650mpNT@cluster0.0pghe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "1002332551805")
CHANNEL_ID = int(getenv("CHANNEL_ID", "1002346012778"))
