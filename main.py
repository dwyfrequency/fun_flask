from flask import Flask, render_template

app = Flask(__name__)

"""Below, mapping two dif urls to the same function,
if the base url is called they will be prompted to login,
else render more detailed info"""
@app.route('/')
@app.route('/<user>')
def hello(user = None):
	return render_template("user.html", user=user)



if __name__ == '__main__':
	app.run(port=5000,debug=True)
