import json
import shelve

import allure
import requests
import pytest
import yaml
from allure_pytest import plugin

@allure.feature("批量开通课包")
class Test:
    # def setup(self):
    #     pass
    # def teardown(self):
    #     pass
    #利用allure插件可以实现标注不同的测试模块
    @allure.story("获取单位id")
    @pytest.mark.parametrize("moblie",yaml.safe_load(open('../批量开通课包/config/yal.yaml')))
    def test_teacher(self,moblie):

        url="https://staging-eduzone.codemao.cn/edu/admin/teachers?page=1"
        # Header={
        #     "cookie":"__ca_uid_key__=7cbeeaf0-4561-4eed-9c9b-4041da995b1e; test_internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6Iue6oumcniIsImVuaWQiOjQxODUsImlhdCI6MTYzMTUyOTgxMiwianRpIjoiNTMxNWJmZmItNDcwMy00OTQyLThhMDAtM2IwY2EyNTM1NjVlIn0.H35zlZyoHj2nx2kYaGE8QSoFmSbAWExLh8O5oyAVmUE; test-admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjg5ODksImlhdCI6MTYzMTUwMTAxMiwianRpIjoiNzBmMDIxMDEtMTQ3Zi0xMWVjLThiYmQtNmQ1ODU2YmFhNTBiIn0.GAGDHtEgHtk6Y45nBJP4IY3a_MhTDN7NkLc9tXOWsXQ; internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6IumDree6oumcniIsImVuaWQiOjE5OTg1LCJpYXQiOjE2MzE2ODY5NzIsImp0aSI6IjcyYWI1Yjk2LWI5NjEtNDJhZC04NzQyLWUyNjQ3ZTQ2ZTBjMyJ9.Uyisy27cPyOLKztAOzOL_GWntOsRzkfeD0hUPRmsP-w; admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjE4NDc2LCJpYXQiOjE2MzE2NTgxNzIsImp0aSI6IjViMzE0MjU2LTE1ZWQtMTFlYy05YjVkLWM3NTYzMDczMjdiNyJ9.gI9uMGCfESTHwx0Ge98kt5LAmxybHeUip5ab1AtDy_U; staging_internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6IumDree6oumcniIsImVuaWQiOjE0ODExLCJpYXQiOjE2MzE2ODcwODQsImp0aSI6IjQwMjI0YWNhLTdhODEtNDRkNy1hODExLTBkMDRjNTQyOTA1ZCJ9.1UMJgHfdrTYDWOdm_EKvAuT-PJMn6Ngg7c-qq3x3To4; staging-admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjEzMjI3LCJpYXQiOjE2MzE2NTgyODQsImp0aSI6IjlkZWVmYmY0LTE1ZWQtMTFlYy05YTk2LWRmNjE4NmJmMWJhMCJ9.Zh-QHVYp12LnLrpEUAF2VpXnwU-9h1oGdp8bNCq5dxg"
        # }
        Header=yaml.safe_load(open('../批量开通课包/config/cookie.yaml'))
        data={
            "mobile":moblie
        }

        res = requests.post(url=url,json=data,headers=Header)
        # print(res.json())
        js = res.json()
        print(js)
        print(type(js))
        H= js["items"][0]["unit_id"]
        print(H)
        #保存用户所对应的单位id
        db = shelve.open("units")
        db['H']=H
        #把生成的单位ID保存起来，这里出现一个问题，只保存了最后一条用例的数据？？
        yaml.safe_dump(js,open("../批量开通课包/config/unit.yaml","w"))
    @allure.feature("获取栏目id")
    @pytest.mark.parametrize("unit",[51178,51126,51113,51115])
    def test_uint(self,unit):
        url="https://staging-eduzone.codemao.cn/edu/admin/lesson/topics"
        # Header={
        #     "cookie":"__ca_uid_key__=7cbeeaf0-4561-4eed-9c9b-4041da995b1e; test-authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJDb2RlbWFvIEF1dGgiLCJ1c2VyX3R5cGUiOiJzdHVkZW50IiwiZGV2aWNlX2lkIjowLCJ1c2VyX2lkIjo1MzQ5MTA1OTgsImlzcyI6IkF1dGggU2VydmljZSIsInBpZCI6IlNqa3FRbWNyIiwiZXhwIjoxNjM1MTU0NzE4LCJpYXQiOjE2MzEyNjY3MTgsImp0aSI6Ijg5OTFmMzcyLWQ0NzgtNDRiNy1hNWI3LWQyN2FlNjAwMTY4ZiJ9.pQA1NRGMJtafzmArlofvCdlTlABmJ7Ole0fd5iEWdfQ; api-test-refresh-token=MTo1MzQ5MTA1OTg6V0VCOkFBQUJlODhTd3Q1d2MySlcyUkI5aEliWVQ5S0ZYcEV3OjIwNmU4NGI5LTgyNzYtNDJmZC04M2Q5LTM2ZmRiNmFjZmE3Mg==; staging_internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6IumDree6oumcniIsImVuaWQiOjE0ODExLCJpYXQiOjE2MzE0OTg3MjAsImp0aSI6ImJmYzE5MDE2LTllZGUtNGZjYS1iMTg5LTI3NTI2MjQyNWQ3MCJ9.GGm7BHjdu7BIU0qalweLCM_qs6dVmiVsGTNR8obAHo0; staging-admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjEzMjI3LCJpYXQiOjE2MzE0Njk5MjAsImp0aSI6IjBjOWU5OTNiLTE0MzctMTFlYy05YTk2LWRmNjE4NmJmMWJhMCJ9.CgpllFuo8Og2xjbjb0mmmTEo1GcJG-a-rY7h2BqDqfw; internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6IumDree6oumcniIsImVuaWQiOjE5OTg1LCJpYXQiOjE2MzE1MTgxODAsImp0aSI6ImMyNWI3YzU1LTUzZjQtNDQ1Yy1hZmIwLWNmN2E5NzcxZmE0YiJ9.fmmCBRlz1mVfjjTYwIuvxmg2gCbR8QcIGY4GTY_7VXM; admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjE4NDc2LCJpYXQiOjE2MzE0ODkzODAsImp0aSI6IjViNjNlMDVjLTE0NjQtMTFlYy05ZTUyLTM1OWVkODJiZDVmMCJ9.ES5qCSkECvGI-J2jn346VT9lDdtQWUO7vOibZeomy8A; api-test-access-token=eyJraWQiOiIyMmZhZjZiNi1lYmMxLTQyMWMtOWJmNS1hNGZhMjQ4NzEwMWQiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJhdGhfY2lkIjoiV0VCIiwic3ViIjoiQ29kZW1hbyBBdXRoIiwiYXRoX3VpZCI6IjUzNDkxMDU5OCIsImF0aF90eXAiOjEsImlzcyI6IkF1dGggU2VydmljZSIsImF0aF92ZXIiOiIxLjAuMCIsImV4cCI6MTYzMTUzNjgzMCwiaWF0IjoxNjMxNTI5NjMwLCJqdGkiOiJBQUFCZTk2LWZMaHdjMkpXMlJCOWs0YllUOUpOVmUxTiJ9.tM5GSndPRkkB4pB_ABnun1TJRto6YG_hA8UGZb0BLy5JZBVioY9dcDFBZfJnnAP6zJrxOPJaN3INC8uSomoUsbCEi_eK9HfxavJN0URv12gJOV-_XiOVc09SNJvIpcz_ueisEVrABglgx9LBzHdNIMeLWPtua504i_FmVKhP5Pj_z_ii_WXQPtRTxROx93I1K1bDra7kJeTR_V0q-MKLgQiVWYh48TFlxFfiepjPt1Ga0PAIPKIK3sWM0WEHgehpqcUs4e5tFRANtnSbWCQ_fIAuwb1mI25bDq3qLAeeOK-2jExD1XoBF1UgmfyA-wcT__0HXhQsr4EAx8cQjGX1XA; api-test-token-type=Bearer; test_internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6Iue6oumcniIsImVuaWQiOjQxODUsImlhdCI6MTYzMTUyOTgxMiwianRpIjoiNTMxNWJmZmItNDcwMy00OTQyLThhMDAtM2IwY2EyNTM1NjVlIn0.H35zlZyoHj2nx2kYaGE8QSoFmSbAWExLh8O5oyAVmUE; test-admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjg5ODksImlhdCI6MTYzMTUwMTAxMiwianRpIjoiNzBmMDIxMDEtMTQ3Zi0xMWVjLThiYmQtNmQ1ODU2YmFhNTBiIn0.GAGDHtEgHtk6Y45nBJP4IY3a_MhTDN7NkLc9tXOWsXQ"
        # }
        Header=yaml.safe_load(open("../批量开通课包/config/cookie.yaml"))
        param={
            "unitId":unit
        }
        res= requests.get(url=url,params=param,headers=Header)
        print(res.json()[0]["id"])
    @allure.feature("获取栏目下的课包")
    @pytest.mark.parametrize("u",[51178,51126,51113,51115])
    def test_lesson(self,u):
        url="https://staging-eduzone.codemao.cn/edu/admin/units/packages/51178/38"
        # Header={
        #     "cookie":"__ca_uid_key__=7cbeeaf0-4561-4eed-9c9b-4041da995b1e; test-authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJDb2RlbWFvIEF1dGgiLCJ1c2VyX3R5cGUiOiJzdHVkZW50IiwiZGV2aWNlX2lkIjowLCJ1c2VyX2lkIjo1MzQ5MTA1OTgsImlzcyI6IkF1dGggU2VydmljZSIsInBpZCI6IlNqa3FRbWNyIiwiZXhwIjoxNjM1MTU0NzE4LCJpYXQiOjE2MzEyNjY3MTgsImp0aSI6Ijg5OTFmMzcyLWQ0NzgtNDRiNy1hNWI3LWQyN2FlNjAwMTY4ZiJ9.pQA1NRGMJtafzmArlofvCdlTlABmJ7Ole0fd5iEWdfQ; api-test-refresh-token=MTo1MzQ5MTA1OTg6V0VCOkFBQUJlODhTd3Q1d2MySlcyUkI5aEliWVQ5S0ZYcEV3OjIwNmU4NGI5LTgyNzYtNDJmZC04M2Q5LTM2ZmRiNmFjZmE3Mg==; staging_internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6IumDree6oumcniIsImVuaWQiOjE0ODExLCJpYXQiOjE2MzE0OTg3MjAsImp0aSI6ImJmYzE5MDE2LTllZGUtNGZjYS1iMTg5LTI3NTI2MjQyNWQ3MCJ9.GGm7BHjdu7BIU0qalweLCM_qs6dVmiVsGTNR8obAHo0; staging-admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjEzMjI3LCJpYXQiOjE2MzE0Njk5MjAsImp0aSI6IjBjOWU5OTNiLTE0MzctMTFlYy05YTk2LWRmNjE4NmJmMWJhMCJ9.CgpllFuo8Og2xjbjb0mmmTEo1GcJG-a-rY7h2BqDqfw; internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6IumDree6oumcniIsImVuaWQiOjE5OTg1LCJpYXQiOjE2MzE1MTgxODAsImp0aSI6ImMyNWI3YzU1LTUzZjQtNDQ1Yy1hZmIwLWNmN2E5NzcxZmE0YiJ9.fmmCBRlz1mVfjjTYwIuvxmg2gCbR8QcIGY4GTY_7VXM; admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjE4NDc2LCJpYXQiOjE2MzE0ODkzODAsImp0aSI6IjViNjNlMDVjLTE0NjQtMTFlYy05ZTUyLTM1OWVkODJiZDVmMCJ9.ES5qCSkECvGI-J2jn346VT9lDdtQWUO7vOibZeomy8A; api-test-access-token=eyJraWQiOiIyMmZhZjZiNi1lYmMxLTQyMWMtOWJmNS1hNGZhMjQ4NzEwMWQiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJhdGhfY2lkIjoiV0VCIiwic3ViIjoiQ29kZW1hbyBBdXRoIiwiYXRoX3VpZCI6IjUzNDkxMDU5OCIsImF0aF90eXAiOjEsImlzcyI6IkF1dGggU2VydmljZSIsImF0aF92ZXIiOiIxLjAuMCIsImV4cCI6MTYzMTUzNjgzMCwiaWF0IjoxNjMxNTI5NjMwLCJqdGkiOiJBQUFCZTk2LWZMaHdjMkpXMlJCOWs0YllUOUpOVmUxTiJ9.tM5GSndPRkkB4pB_ABnun1TJRto6YG_hA8UGZb0BLy5JZBVioY9dcDFBZfJnnAP6zJrxOPJaN3INC8uSomoUsbCEi_eK9HfxavJN0URv12gJOV-_XiOVc09SNJvIpcz_ueisEVrABglgx9LBzHdNIMeLWPtua504i_FmVKhP5Pj_z_ii_WXQPtRTxROx93I1K1bDra7kJeTR_V0q-MKLgQiVWYh48TFlxFfiepjPt1Ga0PAIPKIK3sWM0WEHgehpqcUs4e5tFRANtnSbWCQ_fIAuwb1mI25bDq3qLAeeOK-2jExD1XoBF1UgmfyA-wcT__0HXhQsr4EAx8cQjGX1XA; api-test-token-type=Bearer; test_internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6Iue6oumcniIsImVuaWQiOjQxODUsImlhdCI6MTYzMTUyOTgxMiwianRpIjoiNTMxNWJmZmItNDcwMy00OTQyLThhMDAtM2IwY2EyNTM1NjVlIn0.H35zlZyoHj2nx2kYaGE8QSoFmSbAWExLh8O5oyAVmUE; test-admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjg5ODksImlhdCI6MTYzMTUwMTAxMiwianRpIjoiNzBmMDIxMDEtMTQ3Zi0xMWVjLThiYmQtNmQ1ODU2YmFhNTBiIn0.GAGDHtEgHtk6Y45nBJP4IY3a_MhTDN7NkLc9tXOWsXQ"
        # }
        Header = yaml.safe_load(open("../批量开通课包/config/cookie.yaml"))
        res= requests.get(url=url,headers=Header)
        print(res.json())
    #自动开通课程
    @allure.feature("开通课包")
    def test_select_lesson(self):
        self.env={
            "default":"pro",
            "test": "test-eduzone.codemao.cn",
            "staging":"staging-eduzone.codemao.cn",
            "pro": "eduzone.codemao.cn"
        }
        print(yaml.safe_load(open("../批量开通课包/config/config.yaml")))
        print(type(self.env[self.env["default"]]))
        url="https://staging-eduzone.codemao.cn/edu/admin/units/packages/lessons"
        #实现不同环境的切换
        t = url.replace("staging-eduzone.codemao.cn",self.env[self.env["default"]])
        print(t)
        Header = yaml.safe_load(open("../批量开通课包/config/cookie.yaml"))
        # Header={
        #     "cookie":"__ca_uid_key__=7cbeeaf0-4561-4eed-9c9b-4041da995b1e; internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6IumDree6oumcniIsImVuaWQiOjE5OTg1LCJpYXQiOjE2MzE1MTgxODAsImp0aSI6ImMyNWI3YzU1LTUzZjQtNDQ1Yy1hZmIwLWNmN2E5NzcxZmE0YiJ9.fmmCBRlz1mVfjjTYwIuvxmg2gCbR8QcIGY4GTY_7VXM; admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjE4NDc2LCJpYXQiOjE2MzE0ODkzODAsImp0aSI6IjViNjNlMDVjLTE0NjQtMTFlYy05ZTUyLTM1OWVkODJiZDVmMCJ9.ES5qCSkECvGI-J2jn346VT9lDdtQWUO7vOibZeomy8A; test_internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6Iue6oumcniIsImVuaWQiOjQxODUsImlhdCI6MTYzMTUyOTgxMiwianRpIjoiNTMxNWJmZmItNDcwMy00OTQyLThhMDAtM2IwY2EyNTM1NjVlIn0.H35zlZyoHj2nx2kYaGE8QSoFmSbAWExLh8O5oyAVmUE; test-admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjg5ODksImlhdCI6MTYzMTUwMTAxMiwianRpIjoiNzBmMDIxMDEtMTQ3Zi0xMWVjLThiYmQtNmQ1ODU2YmFhNTBiIn0.GAGDHtEgHtk6Y45nBJP4IY3a_MhTDN7NkLc9tXOWsXQ; staging_internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6IumDree6oumcniIsImVuaWQiOjE0ODExLCJpYXQiOjE2MzE2MDA2MjQsImp0aSI6Ijc5ZjI0MTU5LWQyN2YtNDdhNy05MzVmLTZlOGQ1YzhkOTA3NyJ9.KiZjRoyr7m_mVZkIWScjS3Oz3Xhkx8Z50Yetw7lvxpQ; staging-admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjEzMjI3LCJpYXQiOjE2MzE1NzE4MjQsImp0aSI6IjUwMGQyZjg2LTE1MjQtMTFlYy05YTk2LWRmNjE4NmJmMWJhMCJ9.ya7hDdpw0KWjeDjrRvRPolN2Bf4dJS-hrnlhHtUfeOY; authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJDb2RlbWFvIEF1dGgiLCJ1c2VyX3R5cGUiOiJzdHVkZW50IiwiZGV2aWNlX2lkIjowLCJ1c2VyX2lkIjoxNDUyOTU5LCJpc3MiOiJBdXRoIFNlcnZpY2UiLCJwaWQiOiJTamtxUW1jciIsImV4cCI6MTYzNTQ5MTU4MiwiaWF0IjoxNjMxNjAzNTgyLCJqdGkiOiI3NjA1OWI1MS05OTVhLTQxMmYtOWI0Zi04MWNiYWQ2MGFiOGYifQ.FwB7ll6M_P-KhMWeFGjJn2aaaS4aeZiBdojOtuoIYps; refresh-token=MToxNDUyOTU5OldFQjpBQUFCZS1NbTVGY2FQVVUteTlfRmVudlB6SjFDbGpBazo1ZDk0ZjY1Yy0yNjNmLTQ2YWEtYmRjOS1iMWY0ODcwMDJiMTY="}
        data = {"lesson_ids": [3789, 3790], "package_id": 348, "unit_id": 51178}

        res= requests.post(url=url,headers=Header,json=data)
        print(res)

    # @pytest.mark.parametrize("a",yaml.safe_load(open("../批量开通课包/config/huanjin.yaml")))
    # def test_lessons(self,a):
    #     print(a)
    #     a="nihao"
    #     b = a.replace('n','hh')
    #     print(b)
    #     url="https://test-eduzone.codemao.cn/edu/admin/official/packages/lessons?package_id=39"



