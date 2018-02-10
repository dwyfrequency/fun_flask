import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return '<h2>Index Page</h2>'

@app.route('/hello')
def hello():
	return '<h1 style="color: blue">Hello World!</h1>'

@app.route('/profile/<username>')
def profile(username):
	return 'Hey there {}'.format(username)

@app.route('/zipcode/<int:zip>')
def zipper(zip):
	return 'Zipcode is {}'.format(zip)


if __name__ == '__main__':
	"""using port 4996 works"""
	#app.run(port=5000,debug=True)
	app.run(port=5000,debug=True)