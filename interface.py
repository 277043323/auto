import time
from threading import Thread
import threading

import requests
import json
# params={'name':'nam','age':18}
# playload ={}
# requests.request(method='get',url='',params=params)
# requests.get()
# requests.post()
#编码
# hh="nihao:hello"
# print(json.dumps(hh))
#解码

#文件上传的接口
#批量发送的接口

#结构化请求体构造json
# palyload ={"exam_name": '',"tab":1,"exam_type":2,"site_id":121}
# data ={"limit":10,"page":1}
# headers={'authorization':'Bearer eyJraWQiOiIyMmZhZjZiNi1lYmMxLTQyMWMtOWJmNS1hNGZhMjQ4NzEwMWQiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJhdGhfY2lkIjoiV0VCIiwic3ViIjoiQ29kZW1hbyBBdXRoIiwiYXRoX3VpZCI6IjEyOTE5NDI4ODkiLCJhdGhfdHlwIjoxLCJpc3MiOiJBdXRoIFNlcnZpY2UiLCJhdGhfdmVyIjoiMS4wLjAiLCJleHAiOjE2MzQ3OTE2MTUsImlhdCI6MTYzNDc4NDQxNSwianRpIjoiQUFBQmZLQy1rRHR3eFcxeGZZMG9YVnpaUDV0a1N1elcifQ.LdnMLEoucrkIwpulVcrLWWyO4qdYTD81EfQJw_DnclqvD6bCkdx9mVV-SGUtb6LrYngUY71DQZ3HqsMyNTOKKHl0AQWsm1joXuWkV9IqvkMDrr-kr61uUSrHkIg6SzyS6S5n6125UOkSb5qXLBdD8vjL4EDZ2tUpbiQdw8Xa0-Xb_7xu_YkhHLAwzd26wB2t4TN8RYYwjZXfQ0c5iDJ5z3HrKK_u3lS9q6lBdtsBLNSDUMwY_k5LMys5UCQtjPGHWkZ1xnaN3HMw497112nSdQkUgISJVxGSM-06BZAql9faIU00PO1BzTqpgmtfixZzSCxEpPl_vksh_v0lB01ggw'}
# r=requests.post(url='https://test-eduexam.codemao.cn/home/edu/examinees/1291942889/exams',data=json(data),headers=headers,params=palyload)
# print(r.json())
# print(r.text)
# print(r.headers)
# print(r.raw)
import yaml
import pytest

t =  yaml.safe_load(open('conf.yaml',"r"))
cookie = t["cookie"]
h= t["test"]["host"]
print(h)

# print(t['authorization'])
# ll="jj"
# y = ll.replace('j', 'k')
# print(y)
#获取系统时间
#https://test-eduexam.codemao.cn/home/common/times?TIME=1634790002757

#检查是否只有一场进行中的考试接口
#https://test-eduexam.codemao.cn/home/edu/examinees/1291942889/check/only?exam_type=2&site_id=121&TIME=1634797434679

#根据用户id获取未来教室学生信息接口
#https://press-eduexam.codemao.cn/home/edu/examinees/{userId}/profile
headers=cookie

# headers={"authorization":"Bearer eyJraWQiOiIyMmZhZjZiNi1lYmMxLTQyMWMtOWJmNS1hNGZhMjQ4NzEwMWQiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJhdGhfY2lkIjoiV0VCIiwic3ViIjoiQ29kZW1hbyBBdXRoIiwiYXRoX3VpZCI6IjEyOTE5NDI4ODkiLCJhdGhfdHlwIjoxLCJpc3MiOiJBdXRoIFNlcnZpY2UiLCJhdGhfdmVyIjoiMS4wLjAiLCJleHAiOjE2MzQ4MDQ2MzQsImlhdCI6MTYzNDc5NzQzNCwianRpIjoiQUFBQmZLR0ZObFZ3eFcxeGZZMG9jMXpaUDV0YnpZYUoifQ.Newe6n3QbnUggkM2PRBiBup7ec9quYqG24lofnJJH8MrXc7aRY_LD0mxxpx_KkDiTOMXS1mTs38OfepqIUBrGfem1XtsDXmUp_-OhZoNKlQ9A28DrRU_1kaaVjgKV_CAZUiN1R3ow0oc169ouK74OVk7gxMRvEoIEVU9SDU3ebQAqaLoNibbLtNHV9oFhVd8e1dpQj5v1jlOHBuKmddoG9X9B_145qSC4eVZ_qbwARGStx27XBXeMGtRfxRm403qGALEc1wiutVrv0fJ_NLn6bK2YSgsXfOpF35nMbRMFuSD2xdFIkIjJdQmVBiFLVX5Dt0lPXEVRReOn4tU0ijf9Q","name":"1"}
data={
    'value':"你好"
}
url = "https://host/home/edu/examinees/1291942889/profile"
r = requests.get(url=url.replace('host',h),headers=headers,data=data)
# print(r.json())
# print(r.text)


def test_sys_time():
    access_token = yaml.safe_load(open('conf.yaml','r'))["sys"]
    host = yaml.safe_load(open('conf.yaml','r'))["test"]["host"]
    adder = "https://test/home/common/times"
    area = adder.replace("test",host)
    r = requests.get(url=area,headers=access_token)
    print(r.json())
    assert r.json()!=time.time()
    # r.json()==time.time()
    # print(time.time())
#多线程执行任务
def test_main():
    for i in range(5):
        num1 = threading.Thread(target=test_sys_time)
        num2 = threading.Thread(target=test_sys_time)
        num1.start()
        num2.start()

# def access():
#     headers=yaml.safe_load(open('conf.yaml','r'))["aaccess"]
#     requests.post(url='https://tets-eduzone.codemao.cn/edu/admin/data/verify/adminUnitBatchOpenLesson',headers=headers)

def test_examinees():
    Headers={
     "authorization":"Bearer eyJraWQiOiIyMmZhZjZiNi1lYmMxLTQyMWMtOWJmNS1hNGZhMjQ4NzEwMWQiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJhdGhfY2lkIjoiV0VCIiwic3ViIjoiQ29kZW1hbyBBdXRoIiwiYXRoX3VpZCI6IjE0MDk5MTYzNDAiLCJhdGhfdHlwIjoxLCJpc3MiOiJBdXRoIFNlcnZpY2UiLCJhdGhfdmVyIjoiMS4wLjAiLCJleHAiOjE2MzUxNTEzOTAsImlhdCI6MTYzNTE0NDE5MCwianRpIjoiQUFBQmZMWXdTVDF3eFcxeGZZMHBUSVdBMjMzQmhJU2cifQ.IyqJaYht29L-d2s3XRWgyoFxN6YlgOY_npnOqrq5Aqpu4wPvWuq4-I3GArgZn9LPOe4oUvQZdKnOi5vh7Sd9bA3vSp_cnWSy_dr6uS_YsweGH3uSzJpinAxEC6tdENrbYWDXiJSL7a8IIJEVesmXOk2Q0GFEgxAjS8nmG9LQvjgoGHNDJZa3RpslbTUl3n5CdMWT_gcMK-1XXAaRudXVpy3oYmLTYuUhIN7uEpnCSdcdUnDO3LBVixaTm40v_QEnkgMGdWUzv4MkTI5ZrWRPBRLumhzbgsKLy8DJb3hjV0nIBertyOMEnUtTky7WyZYNnxg7fGjD89HAgom848WDZw"
    }
    datas={"limit":10,"page":1}
    r = requests.post(url="https://test-eduexam.codemao.cn/home/edu/examinees/1409916340/exams?exam_name=&tab=2&exam_type=2&site_id=121",headers=Headers,json=datas)
    print(r.json()['items'][0]['exam_name'])
    # print(r.json().keys())
    # k=r.json().keys()
    # keys = [key for key in k]

def test_one():
    headers={
        'authorization': "Bearer eyJraWQiOiIyMmZhZjZiNi1lYmMxLTQyMWMtOWJmNS1hNGZhMjQ4NzEwMWQiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJhdGhfY2lkIjoiV0VCIiwic3ViIjoiQ29kZW1hbyBBdXRoIiwiYXRoX3VpZCI6IjE0MDk5MTYzNDAiLCJhdGhfdHlwIjoxLCJpc3MiOiJBdXRoIFNlcnZpY2UiLCJhdGhfdmVyIjoiMS4wLjAiLCJleHAiOjE2MzUxNTEzOTAsImlhdCI6MTYzNTE0NDE5MCwianRpIjoiQUFBQmZMWXdTVDF3eFcxeGZZMHBUSVdBMjMzQmhJU2cifQ.IyqJaYht29L - d2s3XRWgyoFxN6YlgOY_npnOqrq5Aqpu4wPvWuq4 - I3GArgZn9LPOe4oUvQZdKnOi5vh7Sd9bA3vSp_cnWSy_dr6uS_YsweGH3uSzJpinAxEC6tdENrbYWDXiJSL7a8IIJEVesmXOk2Q0GFEgxAjS8nmG9LQvjgoGHNDJZa3RpslbTUl3n5CdMWT_gcMK - 1XXAaRudXVpy3oYmLTYuUhIN7uEpnCSdcdUnDO3LBVixaTm40v_QEnkgMGdWUzv4MkTI5ZrWRPBRLumhzbgsKLy8DJb3hjV0nIBertyOMEnUtTky7WyZYNnxg7fGjD89HAgom848WDZw"
    }
    r = requests.get(url='https://test-eduexam.codemao.cn/home/exams/check/2094',headers=headers)

    print(r.json())


def test_two():
    from threading import Thread
    from http import client
    import requests
    #更换请求协议
    client.HTTPConnection._http_vsn = 2.0

    client.HTTPConnection._http_vsn_str = 'HTTP/2.0'
    a = requests.get(url='http://192.168.174.1:8080/aa')
    b = requests.get(url='http://192.168.174.1:8080/index.html')
    print(a.content)
    print(b.content)


# def test_three():
#     conn="Connection"
#     # a = conn.lower()
#     # print(a)
#     # if conn and "close" in conn.lower():
#     #     # print(type(conn.lower()))
#     #     return True
#     if "close" in conn.lower():
#         return True
#     return False
#
# def test_four():
#     print("ss".isspace())

import json
def  test03():
    value='__ca_uid_key__=8b6590b6-d0d5-40fb-929a-d09ed6558682; test_internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6Iue6oumcniIsImVuaWQiOjQxODUsImlhdCI6MTYzNzczNTU5MywianRpIjoiZTc0ODI2NWMtMGE5Yi00OGVhLWI3ODAtNjg2OWUxNWYyNjM1In0.gR9x60E9RZGE_872W3hG84FmI4_bNSUKJC-8ll32V7E; test-admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjg5ODksImlhdCI6MTYzNzcwNjc5MywianRpIjoiNjY1NjgxNjktNGNmMC0xMWVjLThmYzQtZjM3ZjFiZDIwMDc2In0.UgfXcylj0Y5YgYJ1frj6bkBqZpXGlmtE_gbkX9zD200; staging_internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6IumDree6oumcniIsImVuaWQiOjE0ODExLCJpYXQiOjE2Mzc3MzY0ODcsImp0aSI6IjE4YzQ1MzAxLTI0YzUtNDJkOC1hMmFlLWYzN2U1MzVhYzVkMiJ9.znTY6YdytWnbNqq3siRKO6qdq3VHG138jXPGApX0NvI; staging-admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjEzMjI3LCJpYXQiOjE2Mzc3MDc2ODcsImp0aSI6IjdiMmNlOTE0LTRjZjItMTFlYy05YTNhLWI5YzcwYzhiMmNlMyJ9.B0WEAIN3aJuRcVm2RYO4MLzXr4GUpFxz9FLuUSTP7Ao; internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6IumDree6oumcniIsImVuaWQiOjE5OTg1LCJpYXQiOjE2Mzc3MzY2NDIsImp0aSI6ImFiYWUzOTgxLTZiYmQtNDYxYi05NTUyLTk1ZWRmZDVmZTIzZiJ9.PrpMoCBlfXpEiwkJZcztxLflnLMACjoLihidPZ1wIsI; admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjE4NDc2LCJpYXQiOjE2Mzc3MDc4NDIsImp0aSI6ImQ3YTZlYjc3LTRjZjItMTFlYy05MmUxLTZkOTY0ZGM1ZDY5YyJ9.F3R5BEYmVop3OwgnzadpVSMh4wXmKyhTqfYzGRQ4_1M; _ga=GA1.2.1934130895.1637737254; sensorsdata2015jssdkcross={"distinct_id":"584853309","first_id":"17d50ac7d1025c-051b2e24a967084-57442618-2073600-17d50ac7d13172","props":{"$latest_traffic_source_type":"直接流量","$latest_search_keyword":"未取到值_直接打开","$latest_referrer":""},"$device_id":"17d50ac7d1025c-051b2e24a967084-57442618-2073600-17d50ac7d13172"}; authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJDb2RlbWFvIEF1dGgiLCJ1c2VyX3R5cGUiOiJzdHVkZW50IiwiZGV2aWNlX2lkIjowLCJ1c2VyX2lkIjoxMzQ1ODA2NDE3LCJpc3MiOiJBdXRoIFNlcnZpY2UiLCJwaWQiOiJTamtxUW1jciIsImV4cCI6MTY0MTcwOTIxMCwiaWF0IjoxNjM3ODIxMjEwLCJqdGkiOiI1ZjNiMGUyMy1iNmVhLTQ0NmQtYTUxZS05YmIwMjZiOGQwZWQifQ.kaicvGNbw3qZLLkTCvkl2-w5ET1aYfTkOEn8yH1Tw-8; refresh-token=MToxMzQ1ODA2NDE3OldFQjpBQUFCZlZYQVlDZUFTcHRvdno4cXJMdGxSai1oZW1hTTpmNjIxMTM0Zi1kYjU2LTQyMTgtODc5Yi01ZmU1YWZmMjcyZmY=; JSESSIONID=19F9077234D958FC5CCE0196E904B7BA; test-authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJDb2RlbWFvIEF1dGgiLCJ1c2VyX3R5cGUiOiJzdHVkZW50IiwiZGV2aWNlX2lkIjowLCJ1c2VyX2lkIjoxNDA5OTE2MzQwLCJpc3MiOiJBdXRoIFNlcnZpY2UiLCJwaWQiOiJlZ0xJSlBnWSIsImV4cCI6MTY0MTcxNzMwMiwiaWF0IjoxNjM3ODI5MzAyLCJqdGkiOiJhNGUzZTU2Mi01OGIyLTRjOGQtOGVjZi1mNDcyMjdmMjViNmYifQ.N-HkQaQaSML9YUDpTIo8-oXapulYOb4e0eOEcObqvbU; api-test-access-token=eyJraWQiOiIyMmZhZjZiNi1lYmMxLTQyMWMtOWJmNS1hNGZhMjQ4NzEwMWQiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJhdGhfY2lkIjoiV0VCIiwic3ViIjoiQ29kZW1hbyBBdXRoIiwiYXRoX3VpZCI6IjE0MDk5MTYzNDAiLCJhdGhfdHlwIjoxLCJpc3MiOiJBdXRoIFNlcnZpY2UiLCJhdGhfdmVyIjoiMS4wLjAiLCJleHAiOjE2Mzc4MzY1MDIsImlhdCI6MTYzNzgyOTMwMiwianRpIjoiQUFBQmZWWTcxMkZ3TWZDbklmYkF0b1dBMjMzRDdXMGcifQ.m_Ea302dN3DiJCG24En5NSN9t1nzA2VuKcjgNvrtXPCtx8017tkxgPY2Qsg6FfBKl3kwSdaas2aAS-94z7c13a_Nc2e4s2VWJKxRwsCgMFBg-aAcUuGYHfq3m_A1P5qMZztgvS4Nmp0jI--_iwem1Izwc89-djcWVRylQUQv6OvbBwqf-jfNifdEBtQmC2Y1Ujrx8VLFrrNdH626N3axzXdlcSKeeNNMSC3CslpgnaN1Qcbof3cG2BNOI7B9wnF5_k6Uq-xEjy4Y5GC6PPE8cCroaDjBkqS2VB2e3UDPU8SDZO2FitPZE8RPLgYwlIUfi3Rz90kxwLzn1TecvZvmmw; api-test-token-type=Bearer; api-test-refresh-token=MToxNDA5OTE2MzQwOldFQjpBQUFCZlZZNzEyRndNZkNuSWZiQXQ0V0EyMzNZbnhHMTplMjgxNGU0NS04MTU1LTRhMDEtODM5Ni02Y2VmZmI2MTE1NGM='
    Hearder={
        "cookie" :value.encode(),
        'accept':"application/json"
    }
    re = requests.get(url="https://test-eduexam.codemao.cn/admin/oj_baskets/run_oj",params={"markingId":236},headers=Hearder)
    print(re)

def test04():
    value = '__ca_uid_key__=8b6590b6-d0d5-40fb-929a-d09ed6558682; test_internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6Iue6oumcniIsImVuaWQiOjQxODUsImlhdCI6MTYzNzczNTU5MywianRpIjoiZTc0ODI2NWMtMGE5Yi00OGVhLWI3ODAtNjg2OWUxNWYyNjM1In0.gR9x60E9RZGE_872W3hG84FmI4_bNSUKJC-8ll32V7E; test-admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjg5ODksImlhdCI6MTYzNzcwNjc5MywianRpIjoiNjY1NjgxNjktNGNmMC0xMWVjLThmYzQtZjM3ZjFiZDIwMDc2In0.UgfXcylj0Y5YgYJ1frj6bkBqZpXGlmtE_gbkX9zD200; staging_internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6IumDree6oumcniIsImVuaWQiOjE0ODExLCJpYXQiOjE2Mzc3MzY0ODcsImp0aSI6IjE4YzQ1MzAxLTI0YzUtNDJkOC1hMmFlLWYzN2U1MzVhYzVkMiJ9.znTY6YdytWnbNqq3siRKO6qdq3VHG138jXPGApX0NvI; staging-admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjEzMjI3LCJpYXQiOjE2Mzc3MDc2ODcsImp0aSI6IjdiMmNlOTE0LTRjZjItMTFlYy05YTNhLWI5YzcwYzhiMmNlMyJ9.B0WEAIN3aJuRcVm2RYO4MLzXr4GUpFxz9FLuUSTP7Ao; internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6IumDree6oumcniIsImVuaWQiOjE5OTg1LCJpYXQiOjE2Mzc3MzY2NDIsImp0aSI6ImFiYWUzOTgxLTZiYmQtNDYxYi05NTUyLTk1ZWRmZDVmZTIzZiJ9.PrpMoCBlfXpEiwkJZcztxLflnLMACjoLihidPZ1wIsI; admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjE4NDc2LCJpYXQiOjE2Mzc3MDc4NDIsImp0aSI6ImQ3YTZlYjc3LTRjZjItMTFlYy05MmUxLTZkOTY0ZGM1ZDY5YyJ9.F3R5BEYmVop3OwgnzadpVSMh4wXmKyhTqfYzGRQ4_1M; _ga=GA1.2.1934130895.1637737254; sensorsdata2015jssdkcross={"distinct_id":"584853309","first_id":"17d50ac7d1025c-051b2e24a967084-57442618-2073600-17d50ac7d13172","props":{"$latest_traffic_source_type":"直接流量","$latest_search_keyword":"未取到值_直接打开","$latest_referrer":""},"$device_id":"17d50ac7d1025c-051b2e24a967084-57442618-2073600-17d50ac7d13172"}; authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJDb2RlbWFvIEF1dGgiLCJ1c2VyX3R5cGUiOiJzdHVkZW50IiwiZGV2aWNlX2lkIjowLCJ1c2VyX2lkIjoxMzQ1ODA2NDE3LCJpc3MiOiJBdXRoIFNlcnZpY2UiLCJwaWQiOiJTamtxUW1jciIsImV4cCI6MTY0MTcwOTIxMCwiaWF0IjoxNjM3ODIxMjEwLCJqdGkiOiI1ZjNiMGUyMy1iNmVhLTQ0NmQtYTUxZS05YmIwMjZiOGQwZWQifQ.kaicvGNbw3qZLLkTCvkl2-w5ET1aYfTkOEn8yH1Tw-8; refresh-token=MToxMzQ1ODA2NDE3OldFQjpBQUFCZlZYQVlDZUFTcHRvdno4cXJMdGxSai1oZW1hTTpmNjIxMTM0Zi1kYjU2LTQyMTgtODc5Yi01ZmU1YWZmMjcyZmY=; JSESSIONID=19F9077234D958FC5CCE0196E904B7BA; test-authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJDb2RlbWFvIEF1dGgiLCJ1c2VyX3R5cGUiOiJzdHVkZW50IiwiZGV2aWNlX2lkIjowLCJ1c2VyX2lkIjoxNDA5OTE2MzQwLCJpc3MiOiJBdXRoIFNlcnZpY2UiLCJwaWQiOiJlZ0xJSlBnWSIsImV4cCI6MTY0MTcxNzMwMiwiaWF0IjoxNjM3ODI5MzAyLCJqdGkiOiJhNGUzZTU2Mi01OGIyLTRjOGQtOGVjZi1mNDcyMjdmMjViNmYifQ.N-HkQaQaSML9YUDpTIo8-oXapulYOb4e0eOEcObqvbU; api-test-access-token=eyJraWQiOiIyMmZhZjZiNi1lYmMxLTQyMWMtOWJmNS1hNGZhMjQ4NzEwMWQiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJhdGhfY2lkIjoiV0VCIiwic3ViIjoiQ29kZW1hbyBBdXRoIiwiYXRoX3VpZCI6IjE0MDk5MTYzNDAiLCJhdGhfdHlwIjoxLCJpc3MiOiJBdXRoIFNlcnZpY2UiLCJhdGhfdmVyIjoiMS4wLjAiLCJleHAiOjE2Mzc4MzY1MDIsImlhdCI6MTYzNzgyOTMwMiwianRpIjoiQUFBQmZWWTcxMkZ3TWZDbklmYkF0b1dBMjMzRDdXMGcifQ.m_Ea302dN3DiJCG24En5NSN9t1nzA2VuKcjgNvrtXPCtx8017tkxgPY2Qsg6FfBKl3kwSdaas2aAS-94z7c13a_Nc2e4s2VWJKxRwsCgMFBg-aAcUuGYHfq3m_A1P5qMZztgvS4Nmp0jI--_iwem1Izwc89-djcWVRylQUQv6OvbBwqf-jfNifdEBtQmC2Y1Ujrx8VLFrrNdH626N3axzXdlcSKeeNNMSC3CslpgnaN1Qcbof3cG2BNOI7B9wnF5_k6Uq-xEjy4Y5GC6PPE8cCroaDjBkqS2VB2e3UDPU8SDZO2FitPZE8RPLgYwlIUfi3Rz90kxwLzn1TecvZvmmw; api-test-token-type=Bearer; api-test-refresh-token=MToxNDA5OTE2MzQwOldFQjpBQUFCZlZZNzEyRndNZkNuSWZiQXQ0V0EyMzNZbnhHMTplMjgxNGU0NS04MTU1LTRhMDEtODM5Ni02Y2VmZmI2MTE1NGM='
    Hearder = {
        "cookie": value.encode(),
        'accept': "application/json"
    }
    jk = requests.get(url="https://test-eduexam.codemao.cn/admin/oj_baskets/progress",params={"markingId":236},headers=Hearder)
    print(jk.json())

#添加到个人中心
def test05():
    res = requests.get(url="https://eduzone.codemao.cn/edu/zone/lesson/offical/person/packages")



