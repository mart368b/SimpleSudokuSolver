from PyQt5.QtWidgets import (QMainWindow, QApplication,QSizePolicy,QFileDialog,
                             QMessageBox,QProgressBar,QRadioButton,QListWidgetItem)
import Template
import numpy as np
class Player(main.Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(Player,self).__init__()
        self.setupUi(self)
    def Run(self):
        self.buttons = [[self.B00,self.B01,self.B02,self.B03,self.B04,self.B05,self.B06,self.B07,self.B08],
                   [self.B10,self.B11,self.B12,self.B13,self.B14,self.B15,self.B16,self.B17,self.B18],
                   [self.B20,self.B21,self.B22,self.B23,self.B24,self.B25,self.B26,self.B27,self.B28],
                   [self.B30,self.B31,self.B32,self.B33,self.B34,self.B35,self.B36,self.B37,self.B38],
                   [self.B40,self.B41,self.B42,self.B43,self.B44,self.B45,self.B46,self.B47,self.B48],
                   [self.B50,self.B51,self.B52,self.B53,self.B54,self.B55,self.B56,self.B57,self.B58],
                   [self.B60,self.B61,self.B62,self.B63,self.B64,self.B65,self.B66,self.B67,self.B68],
                   [self.B70,self.B71,self.B72,self.B73,self.B74,self.B75,self.B76,self.B77,self.B78],
                   [self.B80,self.B81,self.B82,self.B83,self.B84,self.B85,self.B86,self.B87,self.B88]]
        self.pushButton.clicked.connect(self.GetTable)
    def GetTable(self):
        self.tablevals = [[self.buttons[i][j].value() for i in range(9)] for j in range(9)]
        print(self.tablevals)
        self.ShowSolution()
    def ShowSolution(self):
        solution = np.random.randint(0,high=5,size=(9,9))
        for i in range(9):
            for j in range(9):
                self.buttons[i][j].setValue(solution[i,j])

if __name__ == "__main__":
    app = QApplication([])
    vp = Player()
    vp.Run()
    vp.show()
    app.exec_()
