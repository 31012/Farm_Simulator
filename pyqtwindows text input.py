import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Name Get")
        self.create_main_layout()
    def create_main_layout(self):
        #components
        self.text_box = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.text_lable = QLabel("Please enter your name")
        #create layout
        self.layout = QVBoxLayout()
        #add widgets to the layout
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.text_lable)
        #create widget to hold layout
        self.widget = QWidget()
        #add the layout to the widget
        self.widget.setLayout(self.layout)
        #set central widget
        self.setCentralWidget(self.widget)
        #connections
        self.submit_button.clicked.connect(self.display_text)
    def display_text(self):
        name = self.text_box.text()
        self.text_lable.setText("Hello {0}!".format(name))
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
