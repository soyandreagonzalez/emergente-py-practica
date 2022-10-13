import win32api
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    win32api.MessageBox(0, 0x00001000)
    return render_template('index.html')

@app.route('/test')
def test():
    win32api.MessageBox(0, 0x00001000)
    return render_template('index.htmle3')

if __name__ == "__main__":
    app.run(debug = True)