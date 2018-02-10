from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World'

@app.route('/profile/<name>')
def profile(name):
	return render_template("profile.html", name=name)

if __name__ == '__main__':
	app.run(port=5000,debug=True)
