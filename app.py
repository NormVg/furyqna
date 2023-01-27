from flask import Flask ,request
from ml import ml_app		
app = Flask(__name__)

@app.route('/qna')
def qna():
    text = str(request.args.get('q'))
    reply = ml_app(text)

    return str(reply)




if __name__ == '__main__':
    app.run()
