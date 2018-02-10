from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
	return '<h2>Index Page: {}</h2>'.format(request.method)

@app.route('/tacomaker', methods=['GET', 'POST'])
def tacomaker():
	if request.method == 'POST':
		return 'You are using POST'
	else:
		return 'You are using GET'


if __name__ == '__main__':
	"""using port 4996 works"""
	#app.run(port=5000,debug=True)
	app.run(port=5000,debug=True)