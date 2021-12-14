from flask import Flask,render_template,request,redirect
import jinja2
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager

#发送邮件
from flask_mail import Mail,Message

from flask_migrate import Migrate
import pymysql
pymysql.install_as_MySQLdb()

app =Flask(__name__)

class Config():
    #这里面的配置字段必须是大写的
   SQLALCHEMY_DATABASE_URI = 'mysql://root:12345678@127.0.0.1:3306/author'
   SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.from_object(Config)
#更新数据-批量添加字典update方法
app.config.update(
    Debug=True,
    Mail_SERVER='smtp.qq.com',
    MAIL_PROT = 465,
    MAIL_USE_TLS=True,
    MAIL_USERNAME="1234567@qq.com",
    MAIL_PASSWORD="123456"
)
mail =Mail(app)

db = SQLAlchemy(app)
manager = Manager(app)
manager.add_command("db")

#创建模型类
class Book(db.Model):
    __tablename__='tbl_books'
    id = db.Column(db.Integer,primary_key=True)
    name =db.Column(db.String(80),unique=True)
    authors_id = db.Column(db.Integer,db.ForeignKey("tbl_author.id"))

#创建表单模板类
class AuthorBookForm():
    pass

#发送邮件视图
@app.route('/')
def get_mail():
    msg =Message("this is a test",sender="1234567@qq.com",recipients=["277043323@qq.com","36022888@qq.com"])
    #编辑邮件内容
    msg.body="Flask test mail"
    mail.send(msg)
    return "Sent Succeed"


class Authors(db.Model):
    __tablename__='tbl_author'
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(128),unique = True)
    Book=db.relationship("Book",backref ="author")

@app.route('/',methods=["GET","POST"])
def index():
    # db.query.all()
    author_li = Authors.query.all()
    hh =str(author_li[0].name)
    return hh,200

    # return render_template("book.html",authors =author_li)

@app.route("/delete_book",methods=["POST"])
def delete_book():
    """删除数据"""
    #前端发送的数据是json数据会解析为字典格式
    res_data = request.get_json()
    book_id = res_data.get("book_id")
    #删除数据
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect()




if __name__=='__main__':
    app.run(host="0.0.0.0",port='5003',debug= True)
    # db.drop_all()
    # db.create_all()
    # author1=Authors(name="罗贯中")
    # author2 =Authors(name="施耐庵")
    # author3=Authors(name="曹雪芹")
    # db.session.add_all([author1,author2,author3])
    # db.session.commit()
    #
    #
    # book1=Book(name="三国演义",authors_id=author1.id)
    # book2 = Book(name="水浒传",authors_id=author2.id)
    # book3 =Book(name="红楼梦",authors_id=author3.id)
    # db.session.add_all([book1,book2,book3])
    # db.session.commit()
    # app.run()




