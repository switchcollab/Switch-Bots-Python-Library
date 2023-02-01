from .clear_conversation import ClearConversation
from .delete_message import DeleteMessage
from .delete_messages_from_user import DeleteMessagesFromUser
from .edit_message import EditMessage
from .flag_message import FlagMessage
from .forward_message import ForwardMessage
from .get_channel_chat_history import GetChannelChatHistory
from .get_group_chat_history import GetGroupChatHistory
from .get_community_media_files import GetCommunityMediaFiles
from .get_community_media_files_by_status import GetCommunityMediaFilesByStatus
from .get_flag_messages import GetFlagMessages
from .flag_message import FlagMessage
from .get_message import GetMessage
from .get_messages_between_users import GetMessagesBetweenUsers
from .get_messages import GetMessages
from .get_unread_messages_count import GetUnreadMessagesCount
from .get_user_media_files import GetUserMediaFiles
from .send_message import SendMessage
from .send_text import SendText
from .reply_message_text import ReplyMessageText
from .reply_message import ReplyMessage
from .edit_message_text import EditMessageText
from .answer_inline_query import AnswerInlineQuery
from .download_media import DownloadMedia


class ChatMethods(
    ClearConversation,
    DeleteMessage,
    DeleteMessagesFromUser,
    EditMessage,
    FlagMessage,
    ForwardMessage,
    GetChannelChatHistory,
    GetGroupChatHistory,
    GetCommunityMediaFiles,
    GetCommunityMediaFilesByStatus,
    GetFlagMessages,
    GetMessage,
    GetMessagesBetweenUsers,
    GetMessages,
    GetUnreadMessagesCount,
    GetUserMediaFiles,
    SendMessage,
    SendText,
    ReplyMessageText,
    ReplyMessage,
    EditMessageText,
    AnswerInlineQuery,
    DownloadMedia,
):
    pass
