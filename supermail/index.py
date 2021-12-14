from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def main():
    return "supermail"

if __name__=='__main__':
    debuge=True
    app.run()
