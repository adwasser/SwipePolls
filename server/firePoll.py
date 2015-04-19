from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/<poll_name>')
def getPoll(poll_name):
	return render_template("client.html", poll_name=poll_name)

@app.route('/admin/<poll_name>')
def adminPoll(poll_name):
	return render_template("admin.html", poll_name=poll_name)

if __name__ == '__main__':
	app.debug = True
	app.run()