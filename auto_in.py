import requests
import yaml
import pytest
def test():
    url="https://eduexam.codemao.cn/admin/marking_baskets/page?markingId=393&page=1&limit=200"
    headers={
        "authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6IumDree6oumcniIsImVuaWQiOjE5OTg1LCJpYXQiOjE2MzkwMTk0NjQsImp0aSI6Ijg2ZGY2ODg3LTQ1ODQtNDkwZS1iODAxLTQ4ODFkMDM0ODY2YyJ9.Yh4ketNglB7gB_B93CsyLyUoxPFCDCRjJii09ncozt8"
    }
    res = requests.request(method="get",url=url,headers=headers)
    datas = res.json()["items"]
    # print(datas)
    l =[]
    for i in range(len(datas)):
        id = datas[i]["id"]
        userId=datas[i]["userId"]
        t=(id,userId)
        i+=1
        l.append(t)
    # print(l)

    t = open('./data8.yaml', "w")
    yaml.safe_dump(l, t)
    text = yaml.safe_load(open('./data8.yaml'))
    answer=[]
    for i in text:
        # print(i)
        id = i[0]
        userid = i[1]
        # print(id,userid)
        url="https://eduexam-service.codemao.cn/judge/baskets/basketId?userId=num"
        # print(str(id))
        new_url= url.replace("basketId",str(id)).replace("num",str(userid))
        json_t= requests.request(method="get",url=new_url)
        ans =json_t.json()['answer']
        answer.append(ans)
    an = open('./data1.yaml',"w")
    yaml.safe_dump(answer,an)
    # print(ans)
    # print(new_url)
    # @pytest.mark.parametrize("(a,b)",(str(id),str(userid)))
    # def test(a,b):
    #     url="https://eduexam-service.codemao.cn/judge/baskets/basketId?userId=num"
    #     new_url =url.replace("basketId",a).replace("num",b)
    #     print(new_url)

# def test():
#     url="https://eduexam-service.codemao.cn/judge/baskets/580819?userId=796191286"
#     requests.request(method="get",url=url.replace())