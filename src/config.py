from envparse import env

env.read_envfile()

GET_IP_URL = env('GET_IP_URL')

CHECK_INTERVAL = int(env('CHECK_INTERVAL', default=2)) * 60

LOG_FILE = env('LOG_FILE', default='.log')

BOT_TOKEN = env('BOT_TOKEN')
ADMIN_ID = env('ADMIN_ID')

MONGO_HOST = env('MONGO_HOST', 'localhost')
MONGO_DB = env('MONGO_DB')
MONGO_USER = env('MONGO_USER', default=None)
MONGO_PASSWORD = env('MONGO_PASSWORD', default=None)
