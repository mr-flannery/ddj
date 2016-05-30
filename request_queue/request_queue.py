import Queue

class RequestQueue:
	queue = Queue.PriorityQueue()

	def addSongToQueue(self, videoId, ip):
		queueElemDict = {
			'ip' : ip,
			'videoId' : videoId,
		}

		queueElemTuple = (self.__getPriorityForIp(ip), queueElemDict)
		self.queue.put(queueElemTuple)

	def __getPriorityForIp(self, ip):
		priority = 0

		for elem in self.queue.queue:
			if ip == elem[1]['ip']:
				priority += 1

		return priority

	def printQueue(self):
		self.queue.queue.sort(key = lambda x: x[0])
		for elem in self.queue.queue:
			print(elem)
		print("\n")

	def dequeueUrl(self):
		if not self.queue.empty():
			return self.queue.get()[1]