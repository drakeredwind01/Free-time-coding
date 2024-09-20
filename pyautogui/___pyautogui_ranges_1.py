import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt


class SearchWindowParameters(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Search Window Parameters')

        # Vertical layout
        vbox = QVBoxLayout()

        # Create sliders and labels for the search window (X1, Y1, X2, Y2)
        self.sliders = {}
        self.labels = {}

        for param in ['X1', 'Y1', 'X2', 'Y2']:
            slider_layout = QHBoxLayout()

            label = QLabel(f'{param}: 0', self)
            slider = QSlider(Qt.Horizontal, self)
            slider.setMinimum(0)
            slider.setMaximum(1920)  # Adjust to your screen resolution width or height
            slider.setValue(0)
            slider.valueChanged.connect(lambda value, p=param: self.updateLabel(p, value))

            slider_layout.addWidget(label)
            slider_layout.addWidget(slider)

            vbox.addLayout(slider_layout)

            self.sliders[param] = slider
            self.labels[param] = label

        # Add a button to copy the values to the clipboard
        copy_button = QPushButton('Copy to Clipboard', self)
        copy_button.clicked.connect(self.copyToClipboard)

        vbox.addWidget(copy_button)

        # Set layout to the widget
        self.setLayout(vbox)

    def updateLabel(self, param, value):
        self.labels[param].setText(f'{param}: {value}')

    def copyToClipboard(self):
        x1 = self.sliders['X1'].value()
        y1 = self.sliders['Y1'].value()
        x2 = self.sliders['X2'].value()
        y2 = self.sliders['Y2'].value()

        # Format the output as pyautogui coordinates
        coordinates = f'({x1}, {y1}), ({x2}, {y2})'
        clipboard = QApplication.clipboard()
        clipboard.setText(coordinates)

        # Inform the user
        self.labels['X1'].setText(f'Copied: {coordinates}')


# Main loop
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SearchWindowParameters()
    win.show()
    sys.exit(app.exec_())
