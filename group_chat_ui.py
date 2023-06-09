from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLineEdit, QScrollArea

class ChatWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.layout = QVBoxLayout()

		self.msg_log = QScrollArea()
		self.msg_log.setWidgetResizable(True)

		self.log_contents = QWidget(self.msg_log)
		self.log_layout = QVBoxLayout(self.log_contents)
		self.log_layout.setSizeConstraint(self.log_layout.SetMinAndMaxSize)
		self.msg_log.setWidget(self.log_contents)

		self.msg_input = QLineEdit()
		self.msg_input.returnPressed.connect(self.send_msg)
		self.send_button = QPushButton('Send')
		self.send_button.clicked.connect(self.send_msg)

		self.layout.addWidget(self.msg_log)
		self.layout.addWidget(self.msg_input)
		self.layout.addWidget(self.send_button)

		self.setLayout(self.layout)

	# Each message in the log is a widget that contains the text and reaction buttons
	def log_msg(self, sender, msg):
		msg_widget = QWidget()
		msg_layout = QHBoxLayout(msg_widget)

		msg_text = QTextEdit()
		msg_text.setText(sender + ": " + msg)
		msg_text.setReadOnly(True)
		msg_text.setFixedHeight(50)

		reactionButton = QPushButton('👍')
		reactionButton.clicked.connect(lambda: self.add_reaction(sender, msg))

		msg_layout.addWidget(msg_text)
		msg_layout.addWidget(reactionButton)

		self.log_layout.addWidget(msg_widget)

	def add_reaction(self, msg, sender):
		self.log_msg('👍', 'You to ' + sender)

	def send_msg(self):
		msg = self.msg_input.text()
		if msg:
			self.log_msg(msg, 'You')
			self.msg_input.clear()

def main():
	app = QApplication([])
	chat = ChatWindow()
	chat.show()
	app.exec()

if __name__ == '__main__':
	main()
