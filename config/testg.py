import pytest
import yaml
from functools import reduce

def add(a,b):
    return a+b


print(reduce(add, [1, 2, 3, 4]))

# print(yaml.safe_load(open("yal.yaml")))
# p = yaml.safe_load(open("yal.yaml"))

# pytest.mark.parametrize("b",yaml.safe_load(open("yal.yaml")))
# def test(b):
#     return b+1
print(yaml.safe_load(open("cookie.yaml")))





