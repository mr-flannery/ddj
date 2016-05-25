# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
from tornado.web import URLSpec as URL
from tornado import gen, httpclient

import os
import Queue
import json

queue = Queue.PriorityQueue()

class RequestHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("templates/request.html")

	def post(self):
		data = json.loads(self.request.body)
		self.write("You have sent: {}".format(data['url'].encode('utf-8')))
		self.finish()

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