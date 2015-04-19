import os
from flask import Flask, request
from flask import render_template
import twitter

app = Flask(__name__)

@app.route('/<poll_name>')
def getPoll(poll_name):
	return render_template("client.html", poll_name=poll_name)

@app.route('/admin/<poll_name>')
def adminPoll(poll_name):
	return render_template("admin.html", poll_name=poll_name)

@app.route('/tweet', methods=['GET', 'POST'])
def tweet():
        '''
        Hard coding in the keys...
        '''
        consumer_key = "kKLAIJt1wGzYYkt7vXrP0rgj7"
        consumer_secret = "TYOJk5S3g6KnO2HKjz8gsrkOYk3d5e0diEwqfRogh5WWZxqrl6"
        access_token = "3182916742-2JSaIVrtJrfL1MeSRtsvlJidKSvdM0jHogij1WC"
        access_secret = "bZUGySqEuNvbtySag52kHlOKehX5acSqiM0MYmfWqOwiI"

        if request.method == 'POST':
                text = request.form.get('text', '')
                poll_name = request.form.get('poll name', '')
        else:
                text = request.args.get('text', '')
                poll_name = request.args.get('poll name', '')
        
        api = twitter.Api(consumer_key=consumer_key, 
                          consumer_secret=consumer_secret, 
                          access_token_key=access_token, 
                          access_token_secret=access_secret) 
        url = "http://firepolls.herokuapp.com/" + poll_name
        status = api.PostUpdate(text + '\n' + url)
 
if __name__ == '__main__':
        port = int(os.environ.get("PORT", 5000))
        # app.run(host='0.0.0.0', port=port)
        app.run()
