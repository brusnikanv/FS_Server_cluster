from flask import Flask, render_template
import data

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/servers')
def servers():
    return render_template('servers.html', servers=data.test_get_servers())


if __name__ == '__main__':
    app.run(debug=True)
