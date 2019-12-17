#!/usr/bin/env python3
import sys


class Test:
    base_data = {'id': 1435072639, 'qa': False, 'last_msg': '我觉得你很赞，让我们开始聊天吧', 'conversation_type': 'be_liked',
                 'updated_at': '12月7日', 'free_chat': False, 'member_conversation': {
            'member': {'id': '26b50a18703fcd4e920d4df333ba8b1f', 'member_id': 28271028,
                       'avatar_url': 'http://img.yidui.me/uploads/member_avatar/avatar/28271028/b6510d71a569913cc76f00ea39a1f9ae.jpg@!normal',
                       'sex': 0, 'location': '河南', 'current_location': {'province': '北京'}, 'nickname': '阿飞', 'age': 26,
                       'height': 170, 'online': 2, 'is_vip': True, 'photo_auth': False, 'video_auth': None, 'vip': True,
                       'logout': False, 'is_matchmaker': True, 'is_trump': False, 'is_audio_cupid': True,
                       'is_small_team_cupid': False, 'rose_count': 52165, 'grade': 'rank_e', 'blind_date_duration': 79,
                       'monologue_status': 0, 'monologue': '弱水三千，只取一瓢。', 'avatar_status': 0, 'birthday': '1993-01-01',
                       'video_auth_success': False, 'is_transgress_black': False, 'is_break_transgress': True},
            'read_at': None, 'unread_count': 1}, 'target_conversation': {
            'member': {'id': '49a4842c0d0562bfbe5830229a7021a9', 'member_id': 51680493,
                       'avatar_url': 'http://img.yidui.me/uploads/member_avatar/avatar/51680493/db47e4c4ab1c1303658be7d0f2757222.jpg@!normal',
                       'sex': 1, 'location': '河南', 'current_location': {'province': '河南'}, 'nickname': '玩命的芹菜',
                       'age': 24, 'height': 0, 'online': 3, 'is_vip': True, 'photo_auth': False, 'video_auth': None,
                       'vip': True, 'logout': False, 'is_matchmaker': False, 'is_trump': False, 'is_audio_cupid': False,
                       'is_small_team_cupid': False, 'rose_count': 0, 'grade': 'rank_d', 'blind_date_duration': 0,
                       'monologue_status': 1, 'monologue': None, 'avatar_status': 0, 'birthday': '1995-01-01',
                       'video_auth_success': False, 'is_transgress_black': False, 'is_break_transgress': False},
            'read_at': '2019-12-07T17:58:35.000+08:00', 'unread_count': 0}, 'live_status': None}

    new_dict = {}

    def test_digui(self, data_dict):
        for k, v in data_dict.items():
            if type(v) == dict:
                self.test_digui(v)
            else:
                self.new_dict[k] = v
        print(k, v)
        return self.new_dict


if __name__ == '__main__':
    test = Test()
    print(test.test_digui(test.base_data))
    # print(type({\"recomId\":\"c4804c1b831a4587a68a63063c05ba36\"}))
