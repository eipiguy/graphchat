from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLineEdit, QScrollArea, QComboBox, QLabel
from time import time

from model import Message

class ChatWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.users = {}
		self.messages = {}
		self.start_time = time()
		self.init_ui()

	def init_ui(self):
		self.layout = QVBoxLayout()

		# Message Window
		self.msg_window = QScrollArea()
		self.msg_window.setWidgetResizable(True)

		self.log_contents = QWidget(self.msg_window)
		self.log_layout = QVBoxLayout(self.log_contents)
		self.log_layout.addStretch(1)

		self.msg_window.setWidget(self.log_contents)

		# Message Input UI Elements
		self.user_selection = QComboBox()
		self.user_selection.addItem('')
		self.user_selection.addItem('new')

		self.msg_input = QLineEdit()
		self.msg_input.returnPressed.connect(self.send)

		self.send_button = QPushButton('Send')
		self.send_button.clicked.connect(self.send)

		# Set up the line layout of input ui elements
		self.input_layout = QHBoxLayout()
		self.input_layout.addWidget(self.user_selection)
		self.input_layout.addWidget(self.msg_input)
		self.input_layout.addWidget(self.send_button)

		self.layout.addWidget(self.msg_window)
		self.layout.addLayout(self.input_layout)

		self.setLayout(self.layout)

	def send(self):
		msg = self.msg_input.text()
		if msg:
			timestamp = time()
			sender = self.user_selection.currentText()
			self.post_msg(timestamp, sender, msg)
			self.msg_input.clear()

	# Each message in the log is a widget that contains the text and reaction buttons
	def post_msg(self, timestamp, sender, msg):
		message = Message(timestamp, sender, msg)
		self.messages[timestamp] = message

		# the message widget is where the author and message text are displayed in the log
		# it is a collection of Qt components to display the message details
		# also has buttons to add standard replies
		msg_widget = QWidget()
		msg_layout = QHBoxLayout(msg_widget)

		author_label = QLabel(sender)
		author_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
		
		msg_text = QTextEdit()
		msg_text.setText(msg)
		msg_text.setReadOnly(True)
		msg_text.setFixedHeight(25)

		reactionButton = QPushButton('👍')
		reactionButton.clicked.connect(
			lambda: message.add_reaction(time(), '👍', msg_widget))

		# Label to display the number of reactions
		reactions_tally = QLabel(str(message.reaction_count))
		msg_widget.reactions_tally = reactions_tally  # Store a reference to the tally label in the message widget

		msg_layout.addWidget(author_label)
		msg_layout.addWidget(msg_text)
		msg_layout.addWidget(reactions_tally)
		msg_layout.addWidget(reactionButton)

		msg_widget.setLayout(msg_layout)
		self.log_layout.addWidget(msg_widget)

		# Scroll to bottom after sending a message
		self.msg_window.verticalScrollBar().setValue(self.msg_window.verticalScrollBar().maximum())


def main():
	app = QApplication([])
	chat = ChatWindow()
	chat.show()
	app.exec()

if __name__ == '__main__':
	main()
