# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
from tornado.web import URLSpec as URL
from tornado import gen, httpclient

import os
import Queue
import json
import re

queue = Queue.PriorityQueue()

class RequestHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("templates/request.html")

	def post(self):
		data = json.loads(self.request.body)
		
		if self.isValidYoutubeUrl(data['url']):
			self.write("Thanks for yor request!")
		else:
			self.write("Not a valid YouTube URL")
		
		self.finish()

	def isValidYoutubeUrl(self, url):
		ytRegex = re.compile("https?://www.youtube.com/watch\?v=[a-zA-Z0-9-_]{11}")
		print(ytRegex.match(url))
		return ytRegex.match(url)

class AdminHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("templates/admin.html")

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}

def make_app():
	return tornado.web.Application([
		URL(r"/", RequestHandler, name = "request"),
		URL(r"/admin", AdminHandler, name = "admin"),
	], debug = True, **settings)

if __name__ == "__main__":
	app = make_app()
	app.listen(8088)
	tornado.ioloop.IOLoop.current().start()