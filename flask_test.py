#Flask test

from flask import Flask

app = Flask(__name__)

@app.route('/')

def welcom():
    html='<html><title>welcome</title>'
    html=html+'<body>welcome</body></html>'
    return html

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')
    
