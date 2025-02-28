from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet')
def greet(name):
    return render_template('success.html',user_name=name)

@app.route('/users')
def users():
    user_list=['Alice','Bob','Charlie']
    return render_template('users.html',users=user_list)

if __name__ == '__main__':
    app.run(debug=True)
