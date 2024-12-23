import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24891943"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8c43549f7b146a43b6cf39c431336ebc")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6073523936"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://asezpag3759:1A095y6F4mupiZc1@cluster0.mldij.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
