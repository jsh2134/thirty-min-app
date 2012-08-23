import urllib2
import json

from flask import Flask
from flask import render_template


app = Flask(__name__)


def get_facebook_search_url(query):
	""" Return Facebook Object Location Search URL """
	return 'https://graph.facebook.com/search?type=post&limit=50&q=%s' % (query)


def get_facebook_entities(url):
	""" Connect to Facebook API and return json """
	resp = urllib2.urlopen(url)
	html = resp.read()
	fb_json = json.loads(html)
	return fb_json


@app.route('/')
@app.route('/<query>')
def display_facebook_images(query='olympics'):

	# Build Facebook URL
	fb_url = get_facebook_search_url(query)
	
	# Get Facebook Reponse
	fb_posts = get_facebook_entities(fb_url)
	
	# Render in a Template
	return render_template('photos.html', query=query, fb_posts=fb_posts)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='localhost')
