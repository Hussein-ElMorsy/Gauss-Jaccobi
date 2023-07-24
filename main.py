import sys

from logic import n_2, n_3, n_4

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator, QIcon
from PyQt5.QtWidgets import QApplication, QLabel, QSlider, QPushButton, QLineEdit, QMessageBox

from hframe import HFrame
from vframe import VFrame


class N_Frame(HFrame):
    def __init__(self, parent):
        HFrame.__init__(self, parent)

        self.n_label = QLabel("Number of variables of your system of equations: ", self)
        self.n_slider = QSlider(self)
        self.n_slider.setOrientation(Qt.Horizontal)
        self.n_slider.setMinimum(2)
        self.n_slider.setMaximum(4)

        self.n_slider.setValue(4)

        self.addWidget(self.n_label)
        self.addWidget(self.n_slider)


class ErrorFrame(HFrame):
    def __init__(self, parent):
        HFrame.__init__(self, parent)

        self.error_label = QLabel("the tolerable error: ", self)
        self.error_lineEdit = QLineEdit(self)
        self.error_lineEdit.setValidator(QDoubleValidator())

        self.addWidget(self.error_label)
        self.addWidget(self.error_lineEdit)


class EquationFrame(VFrame):
    def __init__(self, parent, n):
        VFrame.__init__(self, parent)

        self.updateFrame(n)

    def updateFrame(self, n):
        self.n = n

        for i in reversed(range(self.layout().count())):
            self.layout().itemAt(i).widget().setParent(None)

        if self.n == 2:
            self.eq1 = HFrame(self)
            self.eq2 = HFrame(self)

            self.eq1x1 = QLineEdit(self)
            self.eq1x2 = QLineEdit(self)
            self.eq1value = QLineEdit(self)

            self.eq2x1 = QLineEdit(self)
            self.eq2x2 = QLineEdit(self)
            self.eq2value = QLineEdit(self)

            self.eq1x1.setValidator(QDoubleValidator())
            self.eq1x2.setValidator(QDoubleValidator())
            self.eq1value.setValidator(QDoubleValidator())
            self.eq2x1.setValidator(QDoubleValidator())
            self.eq2x2.setValidator(QDoubleValidator())
            self.eq2value.setValidator(QDoubleValidator())

            self.eq1.addWidget(self.eq1x1)
            self.eq1.addWidget(self.eq1x2)
            self.eq1.addWidget(self.eq1value)
            self.eq2.addWidget(self.eq2x1)
            self.eq2.addWidget(self.eq2x2)
            self.eq2.addWidget(self.eq2value)

            self.addWidget(self.eq1)
            self.addWidget(self.eq2)
        elif self.n == 3:
            self.eq1 = HFrame(self)
            self.eq2 = HFrame(self)
            self.eq3 = HFrame(self)

            self.eq1x1 = QLineEdit(self)
            self.eq1x2 = QLineEdit(self)
            self.eq1x3 = QLineEdit(self)
            self.eq1value = QLineEdit(self)
            self.eq2x1 = QLineEdit(self)
            self.eq2x2 = QLineEdit(self)
            self.eq2x3 = QLineEdit(self)
            self.eq2value = QLineEdit(self)
            self.eq3x1 = QLineEdit(self)
            self.eq3x2 = QLineEdit(self)
            self.eq3x3 = QLineEdit(self)
            self.eq3value = QLineEdit(self)

            self.eq1x1.setValidator(QDoubleValidator())
            self.eq1x2.setValidator(QDoubleValidator())
            self.eq1x3.setValidator(QDoubleValidator())
            self.eq1value.setValidator(QDoubleValidator())
            self.eq2x1.setValidator(QDoubleValidator())
            self.eq2x2.setValidator(QDoubleValidator())
            self.eq2x3.setValidator(QDoubleValidator())
            self.eq2value.setValidator(QDoubleValidator())
            self.eq3x1.setValidator(QDoubleValidator())
            self.eq3x2.setValidator(QDoubleValidator())
            self.eq3x3.setValidator(QDoubleValidator())
            self.eq3value.setValidator(QDoubleValidator())

            self.eq1.addWidget(self.eq1x1)
            self.eq1.addWidget(self.eq1x2)
            self.eq1.addWidget(self.eq1x3)
            self.eq1.addWidget(self.eq1value)
            self.eq2.addWidget(self.eq2x1)
            self.eq2.addWidget(self.eq2x2)
            self.eq2.addWidget(self.eq2x3)
            self.eq2.addWidget(self.eq2value)
            self.eq3.addWidget(self.eq3x1)
            self.eq3.addWidget(self.eq3x2)
            self.eq3.addWidget(self.eq3x3)
            self.eq3.addWidget(self.eq3value)

            self.addWidget(self.eq1)
            self.addWidget(self.eq2)
            self.addWidget(self.eq3)
        elif self.n == 4:
            self.eq1 = HFrame(self)
            self.eq2 = HFrame(self)
            self.eq3 = HFrame(self)
            self.eq4 = HFrame(self)

            self.eq1x1 = QLineEdit(self)
            self.eq1x2 = QLineEdit(self)
            self.eq1x3 = QLineEdit(self)
            self.eq1x4 = QLineEdit(self)
            self.eq1value = QLineEdit(self)
            self.eq2x1 = QLineEdit(self)
            self.eq2x2 = QLineEdit(self)
            self.eq2x3 = QLineEdit(self)
            self.eq2x4 = QLineEdit(self)
            self.eq2value = QLineEdit(self)
            self.eq3x1 = QLineEdit(self)
            self.eq3x2 = QLineEdit(self)
            self.eq3x3 = QLineEdit(self)
            self.eq3x4 = QLineEdit(self)
            self.eq3value = QLineEdit(self)
            self.eq4x1 = QLineEdit(self)
            self.eq4x2 = QLineEdit(self)
            self.eq4x3 = QLineEdit(self)
            self.eq4x4 = QLineEdit(self)
            self.eq4value = QLineEdit(self)

            self.eq1x1.setValidator(QDoubleValidator())
            self.eq1x2.setValidator(QDoubleValidator())
            self.eq1x3.setValidator(QDoubleValidator())
            self.eq1x4.setValidator(QDoubleValidator())
            self.eq1value.setValidator(QDoubleValidator())
            self.eq2x1.setValidator(QDoubleValidator())
            self.eq2x2.setValidator(QDoubleValidator())
            self.eq2x3.setValidator(QDoubleValidator())
            self.eq2x4.setValidator(QDoubleValidator())
            self.eq2value.setValidator(QDoubleValidator())
            self.eq3x1.setValidator(QDoubleValidator())
            self.eq3x2.setValidator(QDoubleValidator())
            self.eq3x3.setValidator(QDoubleValidator())
            self.eq3x4.setValidator(QDoubleValidator())
            self.eq3value.setValidator(QDoubleValidator())
            self.eq4x1.setValidator(QDoubleValidator())
            self.eq4x2.setValidator(QDoubleValidator())
            self.eq4x3.setValidator(QDoubleValidator())
            self.eq4x4.setValidator(QDoubleValidator())
            self.eq4value.setValidator(QDoubleValidator())

            self.eq1.addWidget(self.eq1x1)
            self.eq1.addWidget(self.eq1x2)
            self.eq1.addWidget(self.eq1x3)
            self.eq1.addWidget(self.eq1x4)
            self.eq1.addWidget(self.eq1value)
            self.eq2.addWidget(self.eq2x1)
            self.eq2.addWidget(self.eq2x2)
            self.eq2.addWidget(self.eq2x3)
            self.eq2.addWidget(self.eq2x4)
            self.eq2.addWidget(self.eq2value)
            self.eq3.addWidget(self.eq3x1)
            self.eq3.addWidget(self.eq3x2)
            self.eq3.addWidget(self.eq3x3)
            self.eq3.addWidget(self.eq3x4)
            self.eq3.addWidget(self.eq3value)
            self.eq4.addWidget(self.eq4x1)
            self.eq4.addWidget(self.eq4x2)
            self.eq4.addWidget(self.eq4x3)
            self.eq4.addWidget(self.eq4x4)
            self.eq4.addWidget(self.eq4value)

            self.addWidget(self.eq1)
            self.addWidget(self.eq2)
            self.addWidget(self.eq3)
            self.addWidget(self.eq4)


class Window(VFrame):
    def __init__(self):
        VFrame.__init__(self)
        self.setWindowTitle("Numerical Solution of Linear Systems of Equations")
        try:
            self.setWindowIcon(QIcon("icon.ico"))
        except Exception as e:
            pass
        self.layout().setAlignment(Qt.AlignTop)

        self.n_frame = N_Frame(self)
        self.error_frame = ErrorFrame(self)
        self.equations_frame = EquationFrame(self, self.n_frame.n_slider.value())
        self.run_button = QPushButton("Run", self)

        self.run_button.clicked.connect(self.run_program)

        self.n_frame.n_slider.valueChanged.connect(lambda v: self.equations_frame.updateFrame(v))

        self.addWidget(self.n_frame)
        self.addWidget(self.error_frame)
        self.addWidget(self.equations_frame)
        self.addWidget(self.run_button)

        self.show()

    def run_program(self):
        if self.n_frame.n_slider.value() == 2:
            result = n_2(
                self.error_frame.error_lineEdit.text(),
                [self.equations_frame.eq1x1.text(), self.equations_frame.eq1x2.text(),
                 self.equations_frame.eq1value.text()],
                [self.equations_frame.eq2x1.text(), self.equations_frame.eq2x2.text(),
                 self.equations_frame.eq2value.text()],
            )

            QMessageBox.about(self, "Numerical Solution of Linear Systems of Equations", result)

        elif self.n_frame.n_slider.value() == 3:
            result = n_3(
                self.error_frame.error_lineEdit.text(),
                [self.equations_frame.eq1x1.text(), self.equations_frame.eq1x2.text(),
                 self.equations_frame.eq1x3.text(), self.equations_frame.eq1value.text()],
                [self.equations_frame.eq2x1.text(), self.equations_frame.eq2x2.text(),
                 self.equations_frame.eq2x3.text(), self.equations_frame.eq2value.text()],
                [self.equations_frame.eq3x1.text(), self.equations_frame.eq3x2.text(),
                 self.equations_frame.eq3x3.text(), self.equations_frame.eq3value.text()],
            )
            QMessageBox.about(self, "Numerical Solution of Linear Systems of Equations", result)

        elif self.n_frame.n_slider.value() == 4:
            result = n_4(
                self.error_frame.error_lineEdit.text(),
                [self.equations_frame.eq1x1.text(), self.equations_frame.eq1x2.text(),
                 self.equations_frame.eq1x3.text(), self.equations_frame.eq1x4.text(),
                 self.equations_frame.eq1value.text()],
                [self.equations_frame.eq2x1.text(), self.equations_frame.eq2x2.text(),
                 self.equations_frame.eq2x3.text(), self.equations_frame.eq2x4.text(),
                 self.equations_frame.eq2value.text()],
                [self.equations_frame.eq3x1.text(), self.equations_frame.eq3x2.text(),
                 self.equations_frame.eq3x3.text(), self.equations_frame.eq3x4.text(),
                 self.equations_frame.eq3value.text()],
                [self.equations_frame.eq4x1.text(), self.equations_frame.eq4x2.text(),
                 self.equations_frame.eq4x3.text(), self.equations_frame.eq4x4.text(),
                 self.equations_frame.eq4value.text()],
            )
            QMessageBox.about(self, "Numerical Solution of Linear Systems of Equations", result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
