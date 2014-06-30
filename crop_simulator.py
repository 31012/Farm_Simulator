import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from radio_button_widget_class import *
from crop_class import *

class CropWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FarmBoyz 2000")
        self.simulated_crop = ""
        #create stacked layout
        self.stacked_layout = QStackedLayout()
        #create widget wrapper
        self.stacked_widget = QWidget()
        #wrap stacks in wrapper
        self.stacked_widget.setLayout(self.stacked_layout)
        #instaniate layouts to stack
        self.create_select_crop_layout()
        self.create_view_crop_layout(self.simulated_crop)
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
        #mount widget 
        self.setCentralWidget(self.select_crop_widget)
        #connections
        self.instantiate_button.clicked.connect(self.instantiate_crop)
        self.instantiate_button.clicked.connect(self.swap_stack)
    def swap_stack(self):
        self.stacked_layout.setCurrentIndex(1)

        #Crop() is a placeholder until my repo is updated
        #Wheat() and Potato() will replace both
    def instantiate_crop(self):
        crop_type = self.crop_radio_buttons.selected_button()
        if crop_type == 1:
            self.simulated_crop = Crop(1,7,6)
        if crop_type == 2:
            self.simulated_crop = Crop(1,4,7)

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
        self.grow_grid.addLayouts(self.status_grid,0,1)
        self.grow_grid.addLayouts(self.manual_grow_button,1,0)
        self.grow_grid.addLayouts(self.automatic_grow_button,1,1)
        #create a widget to display the grow layout
        self.view_crop_widget = QWidget()
        self.view_crop_widget.setLayout(self.grow_grid)
        

        
        
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = CropWindow()
    window.show()
    window.raise_()
    application.exec_()
