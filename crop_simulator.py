import sys
import random
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from radio_button_widget_class import *
from potato_class import *
from wheat_class import *


class CropWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FarmBoyz 2000")
        #create stacked layout
        self.stacked_layout = QStackedLayout()
        #create widget wrapper
        self.stacked_widget = QWidget()
        #wrap stacks in wrapper
        self.stacked_widget.setLayout(self.stacked_layout)
        #instaniate layouts to stack
        self.create_select_crop_layout()
        #set index of stack
        self.stacked_layout.setCurrentIndex(0)
        #mount widget
        self.setCentralWidget(self.stacked_widget)
        
    def create_select_crop_layout(self):
        #initial layout of the window to selectt crop
        self.crop_radio_buttons = RadioButtonWidget("Crop Simulation", "Please select a crop",("Wheat", "Potato"))
        self.instantiate_button = QPushButton("Create Crop")
        #create layout to hold widgets
        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.crop_radio_buttons)
        self.initial_layout.addWidget(self.instantiate_button)
        self.select_crop_widget = QWidget()
        self.select_crop_widget.setLayout(self.initial_layout)
        #mount widget to stack
        self.stacked_layout.addWidget(self.select_crop_widget)
        #connections
        self.instantiate_button.clicked.connect(self.instantiate_crop)
        
    def instantiate_crop(self):
        crop_type = self.crop_radio_buttons.selected_button()
        if crop_type == 1:
            self.simulated_crop = Wheat()
        if crop_type == 2:
            self.simulated_crop = Potato()
        #instantiate view crop
        self.create_view_crop_layout(crop_type)
        #add widget to stack
        self.stacked_layout.addWidget(self.view_crop_widget)
        #change index
        self.stacked_layout.setCurrentIndex(1)

    def create_view_crop_layout(self,crop_type):
        #second layout window - veiw the crop growth
        #labels
        self.growth_label = QLabel("Growth")
        self.days_label = QLabel("Days growing")
        self.status_label = QLabel("Crop Status")
        #textboxes
        self.growth_line_edit = QLineEdit()
        self.days_line_edit = QLineEdit()
        self.status_line_edit = QLineEdit()  
        #buttons
        self.manual_grow_button = QPushButton("Manually Grow")
        self.auto_grow_button = QPushButton("Automatically Grow")
        #gridlayout
        self.grow_grid = QGridLayout()
        self.status_grid = QGridLayout()
        #add labels to the status layout
        self.status_grid.addWidget(self.growth_label,0,0)
        self.status_grid.addWidget(self.days_label,1,0)
        self.status_grid.addWidget(self.status_label,2,0)
        #add line edit widgets to status layout
        self.status_grid.addWidget(self.growth_line_edit,0,1)
        self.status_grid.addWidget(self.days_line_edit,1,1)
        self.status_grid.addWidget(self.status_line_edit,2,1)
        #add widgets to the grow layout
        self.grow_grid.addLayout(self.status_grid,0,1)
        self.grow_grid.addWidget(self.manual_grow_button,1,0)
        self.grow_grid.addWidget(self.auto_grow_button,1,1)
        #create a widget to display the grow layout
        self.view_crop_widget = QWidget()
        self.view_crop_widget.setLayout(self.grow_grid)
        #connections
        self.auto_grow_button.clicked.connect(self.auto_grow_crop)

    def auto_grow_crop(self):
        for day in range(30):
            light = random.randint(1,10)
            water = random.randint(1,10)
            self.simulated_crop.grow(light,water)
        self.update_crop_veiw_status()
        
    def update_crop_veiw_status(self):
        crop_status_report = self.simulated_crop.report()
        #update text
        self.growth_line_edit.setText(str(crop_status_report["growth"]))
        self.days_line_edit.setText(str(crop_status_report["days growing"]))
        self.status_line_edit.setText(str(crop_status_report["status"]))
        
        
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = CropWindow()
    window.show()
    window.raise_()
    application.exec_()
