from flask import Flask, Response, make_response
from pprint import pprint

class MyResponse(Response):
  
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.headers['Server'] = ""
    pass


app = Flask(__name__)
app.response_class = MyResponse


@app.route('/')
def hello_world():
    resp = MyResponse("hello", status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
#    resp.headers['Server'] = ""
    attrs = vars(resp)

    print(type(resp))
    print( ', '.join("%s: %s" % item for item in attrs.items()))
    print( 'Response : ', str(resp))
    return resp


@app.route("/hello")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
