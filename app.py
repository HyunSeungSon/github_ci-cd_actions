import flask

app = flask.Flask (__name__)

def hello_world():
    return 'hi'

    
if __name__=="__main__":
    app.run(host='0.0.0.0', port='5000')