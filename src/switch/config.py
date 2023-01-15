import os


APP_CONFIG = None


def get_config():
    return APP_CONFIG


def reload_config():
    return {
        "CHAT_SERVICE": {
            "BASE_URL": os.getenv("CHAT_SERVICE_BASE_URL") or "http://51.159.11.53:9999",
            "WS_URL": os.getenv("CHAT_SERVICE_WS_URL")
            or "ws://51.158.56.0:8080/v1/websocket/message",
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
            or "ws://51.159.11.53:9999/v1/websocket/community",
        },
    }


APP_CONFIG = reload_config()
