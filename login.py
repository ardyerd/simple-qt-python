import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from login_form import Ui_loginForm

class Login(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_loginForm()
        self.ui.setupUi(self)

        self.ui.loginButton.clicked.connect(self.auth)

        self.show()

    def auth(self):
        username = self.ui.usernameLineEdit.text()
        password = self.ui.passwordLineEdit.text()

        if username == 'johndoe' and password == '123456':
            QMessageBox.information(self, 'Success',"You're logged in!")
        else:
            QMessageBox.critical(self, 'Error',"Invalid password.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Login()
    sys.exit(app.exec())