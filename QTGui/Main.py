from PyQt5 import QtWidgets
import sys
import MainView

#membuat pewarisan pada Python, dalam kasus ini class Main mewarisi class MainView
#langkah ini dilakukan agar kita dapat melakukan modifikasi pada class MainView tanpa harus mengubah pada class tersebut
#cukup melakukan modifikasi pada class Main
class Main(QtWidgets.QMainWindow, MainView.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        #setupUi merupakan fungsi dari class MainView yang berfungsi untuk melakukan setup
        #sesuai dengan apa yang telah didefinisikan sebelumnya
        self.setupUi(self)
        #jalankan fungsi setValue ketika setButtton diclick
        self.setButton.clicked.connect(self.setValue)

    #definisikan fungsi setValue
    def setValue(self):
    #set nilai setLabel dengan nilai setTextEdit
        self.setLabel.setText(self.setTextEdit.toPlainText())

def main():
    app = QtWidgets.QApplication(sys.argv)  #buat instance baru QtGui
    winForm = Main()                    #inisialisasi variable winForm sebagain class Main
    winForm.show()                      #tampilkan windows form
    sys.exit(app.exec_())               #eksekusi applikasi

if __name__ == '__main__':              #jika file dijalanakan secara langsung, maka jalankan fungsi main()
    main()
