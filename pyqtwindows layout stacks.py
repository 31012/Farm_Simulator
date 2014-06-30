import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        #create stacked layout
        self.stacked_layout = QStackedLayout()
        #create widget to hold layout
        self.stacked_widget = QWidget()
        #add layout to widget
        self.stacked_widget.setLayout(self.stacked_layout)
        #instantiate layouts to stack
        self.create_main_layout()
        self.create_hello_layout()
        #set index of stacked layouts (this is dependant on order layouts
        #were instantated)
        self.stacked_layout.setCurrentIndex(0)
        #"center" layout
        self.setCentralWidget(self.stacked_widget)
    def create_main_layout(self):
        #components
        self.text_box = QLineEdit()
        self.submit_button = QPushButton("Submit")
        #create layout
        self.layout = QVBoxLayout()
        #add widgets to the layout
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.submit_button)
        #create widget to hold layout
        self.widget = QWidget()
        #add the layout to the widget
        self.widget.setLayout(self.layout)
        #add to stacked layout
        self.stacked_layout.addWidget(self.widget)
        #connections
        self.submit_button.clicked.connect(self.switch_layout_to_1)
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
        #add to stacked layout
        self.stacked_layout.addWidget(self.hello_widget)
        #connections
        self.back_button.clicked.connect(self.switch_layout_to_0)

    def switch_layout_to_1(self):
        self.stacked_layout.setCurrentIndex(1)
        name = self.text_box.text()
        self.lable.setText("Hello {0}!".format(name))
    def switch_layout_to_0(self):
        self.stacked_layout.setCurrentIndex(0)
        self.text_box.clear()
        
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
