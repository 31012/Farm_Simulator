import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.create_hello_layout()
    def create_hello_layout(self):
        #components
        self.lable = QLabel()
        self.back_button = QPushButton("Back")
        #create layout
        self.hello_layout = QVBoxLayout()
        #add widgets to layout
        self.hello_layout.addWidget(self.lable)
        self.hello_layout.addWidget(self.back_button)
        #create widget to hold layout
        self.hello_widget = QWidget()
        #add the layout to the widget
        self.hello_widget.setLayout(self.hello_layout)
        self.setCentralWidget(self.hello_widget)
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
