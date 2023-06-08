import time

class User:
	def __init__(self, username, user_id, is_moderator=False):
		self.user_id = user_id
		self.username = username

class Moderator(User):
	def __init__(self):
		pass
	def propose_topic(self):
		pass
	def select_topic(self):
		pass

class Participant(User):
	def __init__(self):
		self.social_health = 0
		pass
	def post_message(self):
		pass
	def vote_topic(self):
		pass

class Message:
	def __init__(self, timestamp, user, text, context=[]):
		self.timestamp = timestamp
		self.author = user
		self.text = text
		self.context = context

class Topic:
	def __init__(self, timestamp, user, text, context=[]):
		self.timestamp = timestamp
		self.author = user
		self.text = text
		self.context_tags = context
		self.votes = []

class Chat:
	def __init__(self):
		self.users = []
		self.messages = []
		self.topics = []

	def add_user(self, user):
		self.users.append(user)

	def remove_user(self, user):
		self.users.remove(user)

	def post_message(self, user, text, context):
		self.messages.append(Message(time.time, user, text, context))