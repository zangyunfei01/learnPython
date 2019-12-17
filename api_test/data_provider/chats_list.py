#!/usr/bin/env python3

"""
喜欢我的人列表页
GET /v2/chats/list
"""

base_response_type = {
    "id": int,
    "qa": bool,
    "last_msg": str,
    "conversation_type": str,
    "updated_at": str,
    "free_chat": bool,
    "member_conversation": {
        "member": {
            "id": str,
            "member_id": int,
            "avatar_url": str,
            "sex": int,
            "location": str,
            "current_location": {
                "province": str
            },
            "nickname": str,
            "age": int,
            "height": int,
            "online": int,
            "is_vip": bool,
            "photo_auth": bool,
            "video_auth": (type(None), str),
            "vip": bool,
            "logout": bool,
            "is_matchmaker": bool,
            "is_trump": bool,
            "is_audio_cupid": bool,
            "rose_count": int,
            "grade": "rank_e",
            "blind_date_duration": int,
            "monologue_status": int,
            "monologue": (type(None), str),
            "avatar_status": int,
            "birthday": str,
            "video_auth_success": bool,
            "is_transgress_black": bool,
            "is_break_transgress": bool
        },
        "read_at": (type(None), str),
        "unread_count": int
    }
}
# "target_conversation": {
#     "member": {
#         "id": "7becf51044895b2105667c14929c255d",
#         "member_id": 74280,
#         "avatar_url": "http://img.yidui.me/public/avatars/default/6.jpg",
#         "sex": 1,
#         "location": "北京",
#         "current_location": {
#             "province": "北京"
#         },
#         "nickname": "杨帅女4",
#         "age": 29,
#         "height": 170,
#         "online": 3,
#         "is_vip": false,
#         "photo_auth": false,
#         "video_auth": null,
#         "vip": false,
#         "logout": false,
#         "is_matchmaker": true,
#         "is_trump": false,
#         "is_audio_cupid": true,
#         "rose_count": 1,
#         "grade": "rank_d",
#         "blind_date_duration": 1111111,
#         "monologue_status": 1,
#         "monologue": null,
#         "avatar_status": 2,
#         "birthday": "1990-01-01",
#         "video_auth_success": false,
#         "is_transgress_black": false,
#         "is_break_transgress": false
#     },
#     "read_at": "2019-11-26T10:11:09.000+08:00",
#     "unread_count": 0
# },
# "live_status": {
#     "scene_type": "VideoRoom",
#     "scene_id": 20,
#     "desc": "视频房间相亲",
#     "simple_desc": "相亲中",
#     "status": "stop",
#     "is_live": false
# }
