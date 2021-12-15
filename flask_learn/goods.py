
#把不同的模块视图进行分开，减少耦合，在主函数中进行调用

# from .main import app
#
# @app.route('/get_goods')
def get_goods():
    return "get goods page"