# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
from tornado.web import URLSpec as URL
from tornado import gen, httpclient
from request_queue import request_queue

import os
import json
import re

requestQueue = request_queue.RequestQueue()

class RequestHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("templates/request.html")

	def post(self):
		data = json.loads(self.request.body)

		if self.isValidYoutubeUrl(data['url']):
			self.write("Thanks for yor request!")
			requestQueue.addSongToQueue(self.getVideoIdFromUrl(data['url']), self.request.remote_ip)
		else:
			self.write("Not a valid YouTube URL")		

		requestQueue.printQueue()

		self.finish()

	def isValidYoutubeUrl(self, url):
		ytRegexLong = re.compile("https?://www.youtube.com/watch\?v=[a-zA-Z0-9-_]{11}")
		ytRegexShort = re.compile("https?://youtu.be/[a-zA-Z0-9-_]{11}")

		if ytRegexLong.match(url) is None and ytRegexShort.match(url) is None:
			return False
		else:
			return True

	def getVideoIdFromUrl(self, url):
		videoIdRegex = re.compile("[a-zA-Z0-9-_]{11}")
		return videoIdRegex.findall(url)[0]

class PlayHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("templates/play.html")

class AdminHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("templates/admin.html")

class UrlHandler(tornado.web.RequestHandler):
	def get(self):
		returnDict = requestQueue.dequeueUrl()
		
		if returnDict is None:
			self.write({
				'videoId' : '',
			})
		else:
			self.write(returnDict)

		self.finish()

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}

def make_app():
	return tornado.web.Application([
		URL(r"/", RequestHandler, name = "request"),
		URL(r"/admin", AdminHandler, name = "admin"),
		URL(r"/play", PlayHandler, name="play"),
		URL(r"/url", UrlHandler),
	], debug = True, **settings)

if __name__ == "__main__":
	app = make_app()
	app.listen(8088)
	tornado.ioloop.IOLoop.current().start()