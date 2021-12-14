from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer,Column
#导入python3中用于链接mysql数据库的驱动程序
import pymysql
pymysql.install_as_MySQLdb()
# from flask_ext.sqlalchemy import SQLAlchemy
import sqlalchemy
app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:12345678@127.0.0.1:3360/testdb'
# #查询时会显示原始数据
# app.config['SQLALCHEMY_ECHO']=True
# db = SQLAlchemy(app)
class Config(object):
    #sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI ='mysql://root:12345678@127.0.0.1:3306/testdb'
    #设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS= True
    #设置sqlalchemy查询数据库的命令



app.config.from_object(Config)
#创建数据库sqlalchemy工具对象
db =SQLAlchemy(app)
#创建模型类,用户表
class User(db.Model):
    __tablename__="tbl_users"
    id = db.Column(db.Integer,primary_key =True)
    name = db.Column(db.String(80),unique=True)
    email=db.Column(db.String(128),unique=True)
    password = db.Column(db.String(128))
    role_id =db.Column(db.Integer,db.ForeignKey("tbl_roles.id"))

    # users=db.relationshin("User",harkref="role")

class Role(db.Model):
    __tablename__="tbl_roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    users = db.relationship("User",backref="role")

if __name__=='__main__':
    app.run()
    # #清除数据库里所有数据
    # db.drop_all()
    # #创建所有的数据表
    # db.create_all()
    # #创建对象
    # role1 = Role(name="admin")
    # #session记录对象任务
    # db.session.add(role1)
    # #提交任务到数据库
    # db.session.commit()
    #
    # role2 = Role(name="stuff")
    # db.session.add(role2)
    # db.session.commit()
    #
    # #一次添加多条数据
    # user1=User(name="wang",email="wang@163.com",password='123456',role_id=role1.id)
    # user2 = User(name="zhang", email="zhang@163.com", password='123', role_id=role2.id)
    # user3 = User(name="chen", email="chen@163.com", password='123456', role_id=role2.id)
    # user4 = User(name="zhou", email="zhou@163.com", password='123', role_id=role1.id)
    # db.session.add_all([user1,user2,user3,user4])
    # db.session.commit()