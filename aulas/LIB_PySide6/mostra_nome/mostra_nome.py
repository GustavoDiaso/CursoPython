from PySide6 import QtWidgets, QtCore, QtGui
import css


class PopUpShowName(QtWidgets.QDialog):
    def __init__(self, name: str):
        super().__init__()
        self.setWindowTitle("Welcome Pop-Up")
        self.setFixedSize(300, 150)

        self.lbl = QtWidgets.QLabel(text=f"Welcome, {name}", parent=self)
        self.lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.layout_ = QtWidgets.QVBoxLayout()
        self.layout_.addWidget(self.lbl)

        self.setLayout(self.layout_)


class MyWindowWidget(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindowWidget, self).__init__()

        self.setWindowTitle("My app")
        self.setFixedSize(400, 300)
        self.setStyleSheet(css.my_window_widget)

        self.main_button = QtWidgets.QPushButton("Push-me", parent=self)
        self.main_button.move(50, 180)
        self.main_button.setStyleSheet(css.main_button)
        self.main_button.clicked.connect(self.show_name)

        self.input_name = QtWidgets.QLineEdit(
            parent=self,
        )
        self.input_name.move(50, 90)
        self.input_name.setStyleSheet(css.input_name)

        self.lbl_name_warning = QtWidgets.QLabel(
            parent=self,
        )

        # This label appears to inform possible mistakes commited by the user while
        # infoming his name
        self.lbl_name_warning.move(50, 130)
        self.lbl_name_warning.setStyleSheet(css.lbl_name_warning)
        self.lbl_name_warning.setVisible(False)

    @QtCore.Slot()
    def show_name(self):
        user_name = self.input_name.text()

        if len(user_name) > 30:
            self.lbl_name_warning.setText("Names must have 30 letters MAX")
            self.lbl_name_warning.setVisible(True)
        elif len(user_name) == 0:
            self.lbl_name_warning.setText("You must inform your name")
            self.lbl_name_warning.setVisible(True)
        else:
            my_popup = PopUpShowName(user_name)
            self.lbl_name_warning.setVisible(False)
            my_popup.exec()


if __name__ == "__main__":
    my_app = QtWidgets.QApplication()
    my_window = MyWindowWidget()

    # torna a nossa tela visível
    my_window.show()

    # Para o código principal e incia o processo de escuta de eventos na nossa UI
    my_app.exec()
