import sys
from PyQt5 import QtWidgets, QtGui
from pyqtpaint import PyQtPaint


class SampleCode(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(SampleCode, self).__init__(*args, **kwargs)
        layout = QtWidgets.QVBoxLayout()

        # create PyQtPaint widget
        paint = PyQtPaint(1920, 1080)

        # set pen attributes
        paint.set_pen_color(QtGui.QColor(80, 230, 140, 255))
        paint.set_pen_size(40)
        paint.set_pen_blur(2)

        layout.addWidget(paint)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    test_window = SampleCode()
    test_window.show()
    sys.exit(app.exec_())
