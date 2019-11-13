#!/usr/bin/env python3
false = False
true = True
null = None


def age(n):
    if n == 1:
        return 18
    else:
        return age(n - 1) + 2


print(age(6))


def calc(n):
    if n % 2 == 0:
        return calc(n / 2)
    else:
        return n


print(calc(10))


def math(n):
    if n % 2 == 0:
        return n
    else:
        return math(n * 3 + 1)


print(math(7))

# for k1, v1 in menu.items():
#     print(k1, ':', v1)
#     if v1 == '' or v1 == {}:
#         print(k1)


# print(type(menu['山东']))


members_dict = {'id': 'a44224a6d8d629efc47d2fd702518ab7', 'member_id': 92674,
                'avatar_url': 'https://img.yidui.me/public/avatars/male/25.jpg', 'sex': 0, 'nickname': '帅呆的凉面',
                'age': 26, 'height': 170, 'is_trump': False, 'monologue_status': 1, 'monologue': None, 'online': 2,
                'vip': False, 'active': '1小时前',
                'current_location': {'province': '北京市', 'city': '北京市', 'district': '朝阳区'}}

complete_type_dict = {}


def get_response_type(new_dict):
    for k in new_dict:
        if type(new_dict[k]) == dict:
            return get_response_type(new_dict[k])
        else:
            complete_type_dict[k] = new_dict[k]
    return complete_type_dict


# print(get_response_type(members_dict))
#
# print(type(members_dict['id']))


test1 = {}

test1['id'] = type(members_dict['id'])

print(type(test1['id']))


# 1 1 2 3 5

def feibo(n):
    l = []
    a, b = 1, 1
    for x in range(n):
        l.append(a)
        a = b
        b = a + b
    print(l[n - 1])
    return l


feibo(10)


# 1,1,2,3,5,8

def feibo2(n):
    if n in (1, 2):
        return 1
    else:
        return feibo2(n - 1) + feibo2(n - 2)


def feibo3(n):
    L3 = []
    for x in range(n):
        if x in (0, 1):
           L3.append(1)
        else:
            L3.append(L3[x - 1] + L3[x - 2])
    print(L3)


feibo3(4)