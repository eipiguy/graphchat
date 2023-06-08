from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit
from PyQt5.QtCore import Qt

class ChatWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		layout = QVBoxLayout()

		self.textArea = QTextEdit()
		self.textArea.setReadOnly(True)

		self.msgInput = QLineEdit()
		self.msgInput.returnPressed.connect(self.sendMsg)

		self.sendButton = QPushButton('Send')
		self.sendButton.clicked.connect(self.sendMsg)

		layout.addWidget(self.textArea)
		layout.addWidget(self.msgInput)
		layout.addWidget(self.sendButton)

		self.setLayout(layout)

	def sendMsg(self):
		msg = self.msgInput.text()
		if msg:
			self.textArea.append("You: " + msg)
			self.msgInput.clear()

def main():
	app = QApplication([])
	chat = ChatWindow()
	chat.show()
	app.exec()

if __name__ == '__main__':
	main()
