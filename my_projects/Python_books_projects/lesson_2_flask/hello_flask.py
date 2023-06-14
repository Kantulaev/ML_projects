import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4',methods=['POST'])
def search4() -> str:
    return 'Rocketman'

@app.route('/time')
def time() -> str:
    return render_template('entry.html',the_title = 'Jopa')
app.run(debug=True)
