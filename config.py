

# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24051078"))
API_HASH = getenv("API_HASH", "5fbd3d24b82a74fb1b0d21fa1d1ce70b")
BOT_TOKEN = getenv("BOT_TOKEN", "7407151388:AAFz3qluZMUYfMDFYDEYrcvuKWhcrXUpGkk")
OWNER_ID = int(getenv("OWNER_ID", "6220013615"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://zennie713:hindi2992@cluster0.uzztvri.mongodb.net")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002227226447"))
FORCESUB = getenv("FORCESUB", "wrgert")
