#!/usr/bin/env python3
import requests
import json


class Recommend:
    user_tags_dict = {}

    def get_user_tags(self, d):
        for k, v in d.items():
            if type(v) == dict:
                self.get_user_tags(v)
            else:
                self.user_tags_dict[k] = v
        # print(self.user_tags_dict)
        return self.user_tags_dict

    def get_users_info(self, l):
        count_ctr = 0
        count_location = 0
        count_A, count_B, count_C, count_D, count_null = 0, 0, 0, 0, 0
        print('返回数据条数：', len(l))
        u_location_list = []
        uctr_list = []
        province_list = []
        hot_tag_list = []
        id_list = []
        for x in range(len(l)):
            for k, v in self.get_user_tags(l[x]).items():
                if k == 'u_location':
                    u_location_list.append(v)
                if k == 'uctr':
                    uctr_list.append(v)
                if k == 'province':
                    province_list.append(v)
                if k == 'hot_tag':
                    hot_tag_list.append(v)
                if k == 'id':
                    id_list.append(v)
        uctr_list_new = []
        for y in uctr_list:
            if y == '无有效ctr':
                count_ctr += 1
            else:
                uctr_list_new.append(y)
        uctr_list_new.sort()
        # print('无有效ctr：', count_ctr)
        u_location_list_new = []
        for z in u_location_list:
            if z == '无':
                count_location += 1
            else:
                u_location_list_new.append(z)
        # print('无城镇信息：', count_location)
        for i in hot_tag_list:
            if i == 'A类':
                count_A += 1
            elif i == 'B类':
                count_B += 1
            elif i == 'C类':
                count_C += 1
            elif i == 'D类':
                count_D += 1
            else:
                count_null += 1
        # return u_location_list, mob_tag_list, uctr_list_new, province_list
        print(
            # ' location:', u_location_list, '\n',
            # 'location_new：', u_location_list_new, '\n',
            # 'uctr：', uctr_list, '\n',
            # 'uctr_new：', uctr_list_new, '\n',
            # 'province："', province_list, '\n',
            'recommend hot tag：', hot_tag_list, '\n'
            'recommend id', id_list, '\n'
            'A：', count_A, ', B：', count_B, ', C：', count_C, ', D：', count_D, "，无：", count_null

        )


if __name__ == '__main__':
    # rpage=tc表示同城，rpage=recom代表首页，
    # envi=stage表示预发布，不写envi默认访问线上
    url = "http://172.16.112.156:9871/preview/recom"
    params = {"apiType": "preview", "uid": 72765684, "rpage": "recom", "envi": ""}

    r = requests.request("GET", url=url, params=params)
    r_body = json.loads(r.text)
    r_my_tag_dict = r_body['resultData']
    r_recommend_tag_dict = r_body['resultObjectList']

    recommend = Recommend()

    my_hot_tag = recommend.get_user_tags(r_my_tag_dict)['hot_tag']
    print('my hot tag:', my_hot_tag)
    recommend.get_users_info(r_recommend_tag_dict)
