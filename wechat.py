from flask import Flask,request,abort

import requests

app=Flask(__name__)

@app.route("/wechat8000")
def wechat():
    #接收服务器发送的参数
    signature = request.args.get("signature")

    #校验参数
    if not signature:
        abort(400)

    #按照微信的流程进行计算签名

@app.route("/wechat8000/index")
def index():
    #获取用户授权时的code
    code=request.args.get("code")
    if not code:
        return u"确实code参数"
    #向微信服务发送http请求，获取access_token
    url="http://api/"

    #向微信服务器发送请求获取用户的资料。