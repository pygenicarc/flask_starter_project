from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    dic = {"name":"kssem", "dept":"CSE"}
    return render_template('index.html', data=dic)


@app.route('/add-task')
def add_task():
    return render_template('add_task.html')


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5005,
        debug=True
    )
