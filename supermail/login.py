from flask import Flask,request,url_for,render_template,redirect,abort,session,g
from werkzeug.routing import BaseConverter
# from flask_script import Manager  #启动命令的管理类

app = Flask(__name__)
#flask中session中需要用到secret_key字符串
app.config['SECRET_KEY']='aggggggggggss'

#创建Manager管理类的对象
# manager= Manager(app=app)
# @app.route('/login',methods=['POST'])
# def login():
#     if request.method=='get':
#         if request.form['username']=='admin':
#             return '欢迎来到接口测试'


@app.route('/',methods=["GET"])
def loginout():
    return "welcome to platform"



def Login_one():
    #url_for函数可以通过视图函数的名字定位到函数的url
    url=url_for("termain")
    return redirect(url)

#在路由中提取参数.
@app.route('/test-explorer.codemao.cn/packageName/<int:id>')
def explorer(id):
    return "这是游戏的信息%d"%id

#自定义转化器
class RegexConverter(BaseConverter):
    def __init__(self,url_map,regex):
        super(BaseConverter,self).__init__(url_map)
        self.regex=regex


#添加自定义转化器到flask应用中
app.url_map.converters["re"]=RegexConverter

# @app.route("/mes/<re(r'^1[3568]/d{11}'):mobile>")
# def send_mes():
#     return "你好"

@app.route('/login',methods=["POST","GET"])
def login_inter():
    if request.method=="POST":
        if request.form.get("name")=="admin" and request.form.get("pwd")=="admin":
            session["name"]=request.get_json()

            return "登录成功",200,{"Access-Control-Allow-Origin":"http://localhost:8080","access-control-allow-methods":"POST","Access-Control-Allow-Credentials":"true","Content-Type":"multipart/form-data;charset=UTF-8"}
        else:
            print(request.form.get("name"),request.form.get("pwd"))
            return "你的用户名或密码错误",403,{"Access-Control-Allow-Origin":"http://localhost:8080","access-control-allow-methods":"POST","Content-Type":"multipart/form-data;charset=UTF-8"}
    else:
        return "请求方式不对"




@app.route("/index",methods=["GET","POST"])
def index():
    if request.method=="GET":
        return "index page",{"Access-Control-Allow-Origin":"http://localhost:8080","access-control-allow-methods":"POST"}
    else:
        return "请查看你的请求方式",{"Access-Control-Allow-Origin":"http://localhost:8080","access-control-allow-methods":"POST"}
#测试终止视图函数abort
@app.route('/termain',methods=["POST","GET"])
def termain():
    return "查看我的信息",{"Access-Control-Allow-Origin":"http://localhost:8080"}

# @app.before_request
# def before_request():
#     print("非debug调试模式下")
#     return "勾子函数的使用"
# @app.after_request
# def after_request(response):
#     print(response)
#     return "哈哈"
#xss跨站脚本攻击，利用前端页面的漏洞来进行攻击，下面给出一个具体的方式
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5002',debug=True)
    #通过管理对象来启动flask
    # manager.run()

