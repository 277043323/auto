from flask import Blueprint

#创建一个蓝图对象，蓝图是一个小模块的概念

app_orders = Blueprint("app_orders",__name__)

@app_orders.route("/get_orders")
def get_orders():
    return "get orders page"


if __name__=='__main__':
    print(app_orders.url_prefix)


