import os


APP_CONFIG = {
    "CHAT_SERVICE": {
        "BASE_URL": os.getenv("CHAT_SERVICE_BASE_URL") or "http://51.159.11.53:9999",
        "WS_URL": os.getenv("CHAT_SERVICE_WS_URL")
        or "ws://51.159.11.53:9999/v1/websocket/message/ws",
    },
    "BOT_SERVICE": {
        "BASE_URL": os.getenv("BOT_SERVICE_BASE_URL") or "http://51.159.11.53:9999",
    },
    "AUTH_SERVICE": {
        "BASE_URL": os.getenv("AUTH_SERVICE_BASE_URL") or "http://51.159.11.53:9999/api",
    },
    "COMMUNITY_SERVICE": {
        "BASE_URL": os.getenv("COMMUNITY_SERVICE_BASE_URL") or "http://51.159.11.53:9999",
        "WS_URL": os.getenv("COMMUNITY_SERVICE_WS_URL")
        or "ws://51.159.11.53:9999/v1/websocket/community/ws",
    },
}


def get_config():
    return APP_CONFIG


def reload_config():
    APP_CONFIG["CHAT_SERVICE"]['BASE_URL'] = os.getenv(
        "CHAT_SERVICE_BASE_URL") or "http://51.159.11.53:9999"
    APP_CONFIG["CHAT_SERVICE"]['WS_URL'] = os.getenv(
        "CHAT_SERVICE_WS_URL") or "ws://51.159.11.53:9999/v1/websocket/message/ws"
    APP_CONFIG["BOT_SERVICE"]['BASE_URL'] = os.getenv(
        "BOT_SERVICE_BASE_URL") or "http://51.159.11.53:9999"
    APP_CONFIG["AUTH_SERVICE"]['BASE_URL'] = os.getenv(
        "AUTH_SERVICE_BASE_URL") or "http://51.159.11.53:9999/api"
    APP_CONFIG["COMMUNITY_SERVICE"]['BASE_URL'] = os.getenv(
        "COMMUNITY_SERVICE_BASE_URL") or "http://51.159.11.53:9999"
    APP_CONFIG["COMMUNITY_SERVICE"]['WS_URL'] = os.getenv(
        "COMMUNITY_SERVICE_WS_URL") or "ws://51.159.11.53:9999/v1/websocket/community/ws"


reload_config()
