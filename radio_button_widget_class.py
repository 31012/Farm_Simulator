from PyQt4.QtGui import *

class RadioButtonWidget(QWidget):
    """this class creates a group of raido buttons from a given list of lables"""
    #Constructor
    def __init__(self,label,instruction,button_list):
        super().__init__()
        #create widgets
        self.title_label = QLabel(label)
        self.radio_group_box = QGroupBox(instruction)
        self.radio_button_group = QButtonGroup()
        #create the raido buttons
        self.radio_button_list = []
        for each in button_list:
            self.radio_button_list.append(QRadioButton(each))
        #set the default checked item
        self.radio_button_list[0].setChecked(True)

        #create layout for radio buttons
        self.radio_button_layout = QVBoxLayout()
        #add buttons o the layout and button group
        counter = 1
        for each in self.radio_button_list:
            self.radio_button_layout.addWidget(each)
            self.radio_button_group.addButton(each)
            self.radio_button_group.setId(each, counter)
            counter += 1
        #add radio buttons to the group box
        self.radio_group_box.setLayout(self.radio_button_layout)
        #create layout for whole widget
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.title_label)
        self.main_layout.addWidget(self.radio_group_box)
        #set the layout for this widget
        self.setLayout(self.main_layout)
    #method to pass on selected button
    def selected_button(self):
        return self.radio_button_group.checkedId()
        
