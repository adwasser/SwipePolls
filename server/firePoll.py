from flask import Flask
from flask import render_template, url_for
app = Flask(__name__)

# url_for('static', filename='main.css')
# url_for('jquery-2.1.3.min.js', filename='jquery-2.1.3.min.js')

@app.route('/<poll_name>')
def getPoll(poll_name):
	return render_template("client.html", poll_name=poll_name)

@app.route('/admin/<poll_name>')
def adminPoll(poll_name):
	return render_template("admin.html", poll_name=poll_name)

if __name__ == '__main__':
	app.debug = True
	app.run()