import os


APP_CONFIG = {
    "CHAT_SERVICE": {
        "BASE_URL": os.getenv("CHAT_SERVICE_BASE_URL") or "https://chat-api.switch.pe",
        "WS_URL": os.getenv("CHAT_SERVICE_WS_URL")
        or "wss://chat-api.switch.pe/v1/websocket/message/ws",
    },
    "BOT_SERVICE": {
        "BASE_URL": os.getenv("BOT_SERVICE_BASE_URL") or "https://chat-api.switch.pe",
    },
    "AUTH_SERVICE": {
        "BASE_URL": os.getenv("AUTH_SERVICE_BASE_URL")
        or "https://gateway.switch.pe/user-service",
    },
    "AIRDROP_SERVICE": {
        "BASE_URL": os.getenv("AIRDROP_SERVICE_BASE_URL")
        or "https://gateway.switch.pe/airdrop-service"
    },
    "COMMUNITY_SERVICE": {
        "BASE_URL": os.getenv("COMMUNITY_SERVICE_BASE_URL")
        or "https://gateway.switch.pe/community-service",
        "WS_URL": os.getenv("COMMUNITY_SERVICE_WS_URL")
        or "wss://gateway.switch.pe/community-service/v1/websocket/community/ws",
    },
    "BACKBLAZE": {
        "BUCKET_ID": os.getenv("BACKBLAZE_BUCKET_ID"),
        "ACCOUNT_ID": os.getenv("BACKBLAZE_ACCOUNT_ID"),
        "APPLICATION_KEY": os.getenv("BACKBLAZE_APPLICATION_KEY")
    }
}


def get_config():
    return APP_CONFIG


def reload_config():
    APP_CONFIG["CHAT_SERVICE"]["BASE_URL"] = (
        os.getenv("CHAT_SERVICE_BASE_URL") or "https://chat-api.switch.pe"
    )
    APP_CONFIG["CHAT_SERVICE"]["WS_URL"] = (
        os.getenv("CHAT_SERVICE_WS_URL")
        or "wss://chat-api.switch.pe/v1/websocket/message/ws"
    )
    APP_CONFIG["BOT_SERVICE"]["BASE_URL"] = (
        os.getenv("BOT_SERVICE_BASE_URL") or "https://chat-api.switch.pe"
    )
    APP_CONFIG["AUTH_SERVICE"]["BASE_URL"] = (
        os.getenv("AUTH_SERVICE_BASE_URL") or "https://gateway.switch.pe/user-service"
    )
    APP_CONFIG["COMMUNITY_SERVICE"]["BASE_URL"] = (
        os.getenv("COMMUNITY_SERVICE_BASE_URL")
        or "https://gateway.switch.pe/community-service"
    )
    APP_CONFIG["COMMUNITY_SERVICE"]["WS_URL"] = (
        os.getenv("COMMUNITY_SERVICE_WS_URL")
        or "wss://gateway.switch.pe/community-service/v1/websocket/community/ws"
    )
    APP_CONFIG["AIRDROP_SERVICE"]["BASE_URL"] = (
        os.getenv("AIRDROP_SERVICE_BASE_URL")
        or "https://gateway.switch.pe/airdrop-service"
    )


reload_config()
