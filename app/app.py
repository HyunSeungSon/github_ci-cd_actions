import flask

app = flask.Flask (__name__)

def hello_world():
    return 'hi'

    
if __name__ == "__main__": 
    print("runnig server")
    app.run(host = "127.0.0.1", port = 5000, debug = True)