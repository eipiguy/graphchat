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
	def __init__(self, timestamp, text, user='', reactions={}, parent=None):
		self.timestamp = timestamp
		self.text = text
		self.author = user
		self.reactions = reactions
		self.reaction_count = self.count_reactions()
		self.heirarchy_lvl = 0
		if parent:
			self.parent = parent
			self.heirarchy_lvl = parent.heirarchy_lvl + 1

	def add_reaction(self, timestamp, msg, msg_widget):
		self.reactions[timestamp] = Message(
			timestamp, msg, user='', reactions={}, parent=self)
		self.reaction_count += 1
		msg_widget.reactions_tally.setText(str(self.reaction_count))

	def count_reactions(self):
		num_reactions = len(self.reactions)
		for reaction in self.reactions.values():
			num_reactions += reaction.count_reactions()
		return num_reactions

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