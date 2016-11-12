#froAm_slack POST

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def welcome():
    html = '<html><title>welcome</title>'
    html = html + '<body>welcome</body></html>'
    return html

@app.route('/matter', methods=['POST'])
def post():
    print (request.form)
    return

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
