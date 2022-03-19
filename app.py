from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World!!</h1>'

@app.route('/slot0')
@app.route('/slot1')
@app.route('/slot2')
@app.route('/slot3')
def setcookie():
   
   
   slot = request.path
   resp = make_response(f'<h1>Setting slot cookie to {slot}</h1>')
   resp.set_cookie('release_slot', slot)
   return resp


@app.route('/getcookie')
def getcookie():

   release_slot = request.cookies.get('release_slot')
   return f'<h1>welcome to {release_slot}</h1>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', ssl_context='adhoc', port=8443)