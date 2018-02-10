from flask import Flask, render_template

app = Flask(__name__)

"""Below, mapping two dif urls to the same function,
if the base url is called they will be prompted to login,
else render more detailed info"""
@app.route('/')
@app.route('/<user>')
def index(user = None):
	return render_template("user.html", user=user)

@app.route('/shopping')
def shopping():
	food = ["salmon", "sweet potato", "oatmeal"]
	return render_template('shopping.html', food=food)

if __name__ == '__main__':
	app.run(port=5000,debug=True)
