from PySide6.QtWidgets import (
    QApplication, QDialog, QMessageBox
)
from untitled import Ui_Dialog
import sys


class MyGenerate(Ui_Dialog, QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton.clicked.connect(
            self.new_password
        )

    def new_password(self):
        word = "mima"
        self.lineEdit.setText(word)
        QMessageBox.information(
            self, "tishi", "chenggong"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myGenerate = MyGenerate()

    sys.exit(app.exec())  # 启动循环
