from flask import Flask,request
from flask_cors import CORS
from flask_learn import goods,order
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
# from .order import app_orders
# from .goods import get_goods
app = Flask(__name__)

#创建配置类
class Config(object):
    SQLALCHEMY_DATABASE_URI="mysql://root:12345678@127.0.0.1:3306/interface_auto"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.from_object(Config)
db =SQLAlchemy(app)
app.register_blueprint(order.app_orders,url_prefix ="/orders")
# from .goods import get_goods
#解决循环调用产生的问题
app.route('/get_goods')(goods.get_goods)
#解决跨域的方法
CORS(app,supports_credentials=True)
#创建测试用例模板对象
class Testcase(db.Model):
    __tablename__='tbl_testcase'
    id = db.Column(db.Integer,primary_key=True)
    case_project = db.Column(db.String(30))
    case_name = db.Column(db.String(30))
    case_detail = db.Column(db.String(128))
    op_case = db.Column(db.String(128))
    expect_ret=db.Column(db.String(60))

#创建项目模块模板对象
class Categ(db.Model):
    __tablename__='tbl_categoric'
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(60))

#设置分类列表接口
@app.route('/catelogric',methods=["GET","POST"])
def Catelogric():
    list =[]
    t= Categ.query.all()
    for i in range(len(t)):
        li =t[i].name
        list.append(li)
    return str(list)

#创建分类视图函数
@app.route("/add_catelogir",methods=["GET","POST"])
def add_catelogir():
    if request.method=="POST":
        if request.data !='':
            li = request.form.get("categ_li")
            obj=Categ(name=li)
            db.session.add(obj)
            db.session.commit()

    return "success"

# @app.route('/',methods=["GET","POST"])
# def index():
#     pass
#
# @app.route('/login',methods=["GET","POST"])
# def login():
#     pass
#创建添加测试用例视图函数
@app.route('/addcase',methods=["GET","POST"])
def AddCase():
    if request.method=="POST":
        if request.data !='':
            #获取表单中的数据并保存在数据库表中
            case_project = request.form.get("case_project")
            print(type(case_project))
            case_name = request.form.get("case_name")
            case_detail = request.form.get("case_detail")
            op_case = request.form.get("op_case")
            expect_ret=request.form.get("expect_ret")
            case1=Testcase(case_project=case_project,case_name=case_name,case_detail=case_detail,op_case=op_case,expect_ret=expect_ret)
            db.session.add(case1)
            db.session.commit()

            Testcase.query.all()
            return "success",{"access-control-allow-credentials":"true","access-control-allow-origin":'http://localhost:8080',"access-control-allow-methods":"POST,GET","Content-Type":"multipart/form-data;charset=UTF-8mb4"}

        else:
            return "please input data",403,{"access-control-allow-credentials":"true","access-control-allow-origin":'http://localhost:8080',"access-control-allow-methods":"POST,GET","Content-Type":"multipart/form-data;charset=UTF-8mb4"}
    else:
        return "methods error",{"access-control-allow-credentials":"true","access-control-allow-origin":'http://localhost:8080',"access-control-allow-methods":"POST,GET","Content-Type":"multipart/form-data;charset=UTF-8mb4"}



if __name__=='__main__':
    # db.drop_all()
    # db.create_all()
    # case2 = Categ(name="山东考试中心")
    # case3 =Categ(name ="济南考试")
    # case4=Categ(name ="江西考试")
    # # db.session.add(case2)
    # db.session.add_all([case2,case3,case4])
    # db.session.commit()

    #
    # case1 = Testcase(case_project="考试系统",case_name="考试配置",case_detail="设置所有的配置",op_case="网站名称",expect_ret="200")
    # db.session.add(case1)
    # db.session.commit()
    # print(app.url_map)
    # app.run
    app.run(debug=True)