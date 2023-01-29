from flask import Flask ,request
from ml import ml_app		
app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return "hello world"

@app.route('/qna', methods=["GET"])
def qna():
    text = str(request.args.get('q'))
    reply = ml_app(text)
    
    return str(reply)


