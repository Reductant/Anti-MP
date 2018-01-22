from flask import Flask, request, session, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/check')
def check():
    return render_template('form.html')


@app.route('/results', methods=['POST'])
def process():
    data = request.form.copy()
    return render_template('results.html', data=data)


if __name__ == '__main__':
    app.run()
