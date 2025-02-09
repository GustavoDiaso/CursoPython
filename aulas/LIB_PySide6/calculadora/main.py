from PySide6 import QtWidgets, QtCore, QtGui
import css
from functools import partial


class CalculatorMainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(350, 500)
        self.setWindowTitle("Calculator")
        self.setStyleSheet(css.main_window)

        self.lbl_expression = QtWidgets.QLabel("", parent=self)
        self.lbl_expression.setStyleSheet(css.lbl_expression)
        self.lbl_expression.move(10, 20)

        self.solution_screen = QtWidgets.QLabel("", parent=self)
        self.solution_screen.setStyleSheet(css.solution_screen)
        self.solution_screen.move(0, 40)
        self.solution_screen.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignVCenter | QtCore.Qt.AlignmentFlag.AlignRight
        )
        self.screen_layout = QtWidgets.QVBoxLayout()
        self.screen_layout.addChildWidget(self.solution_screen)

        self.number_layout_box = QtWidgets.QWidget(parent=self)
        self.number_layout_box.setStyleSheet(css.number_layout_box)
        self.number_layout_box.move(8, 160)
        self.number_layout = CalculatorButtonsLayout(
            self, parent=self.number_layout_box
        )


# ----------------------------------------------------------


class CalculatorButtonsLayout(QtWidgets.QGridLayout):
    def __init__(self, calculator_window: CalculatorMainWindow, parent):
        super().__init__(parent)
        # setting the default configurations
        self.setSpacing(0),
        self.setContentsMargins(0, 0, 0, 0)

        # calculator_window referes to the calculator this Grid is related to
        self.calculator_window = calculator_window

        self.special_btn_icons = {
            "%": None,
            "CE": self.clear_whole_operation,
            "C": self.clear_display,
            "⌫": self.remove_num_from_display,
            "¹/x": None,
            "x²": None,
            "√x": None,
            "÷": partial(self.insert_math_sign, "/"),
            "*": partial(self.insert_math_sign, "*"),
            "-": partial(self.insert_math_sign, "-"),
            "+": partial(self.insert_math_sign, "+"),
            "±": None,
            ".": None,
            "=": self.get_solution,
        }

        self.special_buttons = []
        for special_icon in self.special_btn_icons.keys():
            # creating the button
            btn = QtWidgets.QPushButton(text=special_icon)
            # applying a css on the button
            btn.setStyleSheet(css.special_button)
            # defining a different cursor shape when hover
            btn.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

            # each button will call the function related to his icon when clicked
            function_related_to_icon = self.special_btn_icons[special_icon]
            if function_related_to_icon is not None:
                btn.clicked.connect(function_related_to_icon)

            self.special_buttons.append(btn)

        self.number_buttons = []
        for number_symbol in range(0, 10):
            # creating the button
            btn = QtWidgets.QPushButton(text=str(number_symbol))
            # applying a css on the button
            btn.setStyleSheet(css.number_button)
            # defining a different cursor shape when hover
            btn.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(partial(self.add_num_to_display, str(number_symbol)))
            self.number_buttons.append(btn)

        # lets add the first 8 special buttons to the layout
        for i in range(0, 4):
            self.addWidget(self.special_buttons[i], 1, i + 1)
        for i in range(4, 8):
            self.addWidget(self.special_buttons[i], 2, i - 3)

        # lets add the rest of the special buttons to the layout
        self.addWidget(self.special_buttons[8], 3, 4)
        self.addWidget(self.special_buttons[9], 4, 4)
        self.addWidget(self.special_buttons[10], 5, 4)
        self.addWidget(self.special_buttons[11], 6, 1)
        self.addWidget(self.special_buttons[12], 6, 3)
        self.addWidget(self.special_buttons[13], 6, 4)

        # Lets add the number buttons to the layout
        self.addWidget(self.number_buttons[0], 6, 2)

        for i in range(1, 4):
            self.addWidget(self.number_buttons[i], 5, i)
        for i in range(4, 7):
            self.addWidget(self.number_buttons[i], 4, i - 3)
        for i in range(7, 10):
            self.addWidget(self.number_buttons[i], 3, i - 6)

    @QtCore.Slot()
    def add_num_to_display(self, number: str):
        if len(self.calculator_window.solution_screen.text()) < 10:
            if self.calculator_window.solution_screen.text() == "":
                self.calculator_window.solution_screen.setText(number)
            else:
                self.calculator_window.solution_screen.setText(
                    "".join([self.calculator_window.solution_screen.text(), number])
                )

    @QtCore.Slot()
    def remove_num_from_display(self):
        if self.calculator_window.solution_screen.text() != "":
            self.calculator_window.solution_screen.setText(
                self.calculator_window.solution_screen.text()[:-1]
            )

    @QtCore.Slot()
    def clear_display(self):
        self.calculator_window.solution_screen.setText("")

    @QtCore.Slot()
    def clear_whole_operation(self):
        self.calculator_window.solution_screen.setText("")
        self.calculator_window.lbl_expression.setText("")

    @QtCore.Slot()
    def insert_math_sign(self, sign: str):
        """iserts the clicked math sign to the math expression"""
        math_signs = ["/", "*", "-", "+"]
        math_signs_count = 0
        for sign_ in math_signs:
            math_signs_count += self.calculator_window.lbl_expression.text().count(
                sign_
            )

        if self.calculator_window.solution_screen.text() != "":
            if math_signs_count == 0:
                self.calculator_window.lbl_expression.setText(
                    "".join([self.calculator_window.solution_screen.text(), sign])
                )
                self.calculator_window.solution_screen.setText("")
            else:
                expression_solution = eval(
                    self.calculator_window.lbl_expression.text()
                    + self.calculator_window.solution_screen.text()
                )

                self.calculator_window.lbl_expression.setText(
                    "".join([str(expression_solution), sign])
                )

                self.calculator_window.solution_screen.setText("")

    @QtCore.Slot()
    def get_solution(self):
        if self.calculator_window.solution_screen.text() != "":
            solution = eval(
                self.calculator_window.lbl_expression.text()
                + self.calculator_window.solution_screen.text(),
            )
            self.calculator_window.lbl_expression.setText(
                self.calculator_window.lbl_expression.text()
                + self.calculator_window.solution_screen.text()
            )
            self.calculator_window.solution_screen.setText(str(solution))
            self.calculator_window.lbl_expression.setText("")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = CalculatorMainWindow()
    window.show()
    app.exec()
