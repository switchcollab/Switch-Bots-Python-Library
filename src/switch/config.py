import os


APP_CONFIG = None


def get_config():
    return APP_CONFIG


def reload_config():
    return {
        "CHAT_SERVICE": {
            "BASE_URL": os.getenv("CHAT_SERVICE_BASE_URL") or "http://51.158.56.0:8080",
            "WS_URL": os.getenv("CHAT_SERVICE_WS_URL") or "ws://51.158.56.0:8080/comm",
        },
        "AUTH_SERVICE": {
            "BASE_URL": os.getenv("AUTH_SERVICE_BASE_URL") or "http://51.159.11.53:9999/api",
        },
        "COMMUNITY_SERVICE": {
            "BASE_URL": os.getenv("COMMUNITY_SERVICE_BASE_URL") or "http://51.159.11.53:9999/api",
            "WS_URL": os.getenv("COMMUNITY_SERVICE_WS_URL") or "ws://51.159.11.53:9999/api/comm",
        },
    }


APP_CONFIG = reload_config()
