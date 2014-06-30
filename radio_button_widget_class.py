from PyQt4.QtGui import *

class RadioButtonWidget(QWidget):
    """this class creates a group of raido buttons from a given list of lables"""
    #Constructor
    def __init__(self,lable,instruction,button_list):
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
            self.radio_button_layout.addWdiget(each)
            self.radio_button_group.addButton(each)
