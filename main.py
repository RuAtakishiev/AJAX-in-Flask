from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    text = request.args.get('button_text')
    print()
    print('Button text:', text)
    print()
    return render_template('index.html')

if __name__ == '__main__':
    app.run()