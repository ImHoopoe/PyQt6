import sys
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QTableWidget,QTableWidgetItem
from Contact import Contact
class Main(QWidget) :
    def __init__(self):
        super().__init__()
        self.UI()
    

    def UI(self) :

        #Table
        self.Contacts_Table = QTableWidget(self)
        self.Contacts_Table.setColumnCount(4)
        self.Contacts_Table.setGeometry(0,0,600,400)
        self.Contacts_Table.setHorizontalHeaderLabels(["نام","نام خانوادگی","شماره تلفن","آدرس"])

        #Buttons
        self.Add_Contact_btn = QPushButton("افزودن",self)
        self.Add_Contact_btn.move(0,150)
        
        self.Edit_Contact_btn = QPushButton("ویرایش",self)
        self.Edit_Contact_btn.move(75,150)

        self.Delete_Contact_btn = QPushButton("حذف",self)
        self.Delete_Contact_btn.move(125,150)

        self.Save_Contact_btn = QPushButton("زخیره تغییرات",self)
        self.Save_Contact_btn.move(0,200)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())