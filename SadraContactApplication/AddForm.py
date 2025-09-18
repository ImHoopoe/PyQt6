import sys
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QTableWidget,QLabel,QTableWidgetItem,QLineEdit

class Main(QWidget) :
    def __init__(self):
        super().__init__()
        self.UI()
    

    def UI(self) :

        #Table
        self.Name_input = QLineEdit(self)
        self.Name_input.move(50,50)
        self.LastName_input = QLineEdit(self)
        self.LastName_input.move(50,75)
        self.PhoneNumber_input = QLineEdit(self)
        self.PhoneNumber_input.move(50,100)
        self.Address_input = QLineEdit(self)
        self.Address_input.move(50,125)

        #labels :
        self.Name_lbl = QLabel("نام",self)
        self.Name_lbl = QLabel("نام خانوادگی",self)
        self.Name_lbl = QLabel("شماره تلفن",self)
        self.Name_lbl = QLabel("آدرس",self)

        #Buttons
        self.Submit_btn = QPushButton("زخیره مخاطب", self)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())