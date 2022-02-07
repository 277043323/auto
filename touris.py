import pytest
import yaml
import requests
#
# def test():
#     #yaml中不能存在中文或则会出现乱码
#     t = yaml.safe_load(open('datatours.yaml'))
#     print(t)

#随机生成100个姓名和性别保存在yaml文件中。
#改进方案

@pytest.mark.parametrize("a",yaml.safe_load(open('datatours.yaml')))
def test01(a):
    data ={"deviceInfo": {"fingerPrint": "22c20ff010813214a"}, "examId": 2234, "siteId": 205,
         "submitterInfo": [{"bizName": "name", "id": 771, "value":a}, {"bizName": "sex", "id": 772, "value": 1}]}
    # print(type(a))
    # print(a)
    # print(data["submitterInfo"][0]["value"])
    res = requests.post(url="https://test-eduexam.codemao.cn/anonymous/home/submitter",json=data)
    # print(res.json())


