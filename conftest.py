import pytest

#autouse设置为true那所有的函数都会自动的调用fixture,不需要手动去添加函数
@pytest.fixture(scope="class")
def login():
    print("我是登录设备")
    yield
    print("第一条测试相关的数据")