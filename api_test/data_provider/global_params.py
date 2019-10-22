#!/usr/bin/env python3
import api_test.data_provider.auth


class GlobalParams:
    Authorization = api_test.data_provider.auth.get_auth()
    MemberId = api_test.data_provider.auth.get_member_id()
