import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QScreen

class SearchWindowParameters(QWidget):
    def __init__(self):
        super().__init__()
        self.screen = QApplication.primaryScreen()

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
            if 'X' in param:
                slider.setMaximum(1920)  # Adjust to your screen resolution width
            else:
                slider.setMaximum(1080)  # Adjust to your screen resolution height
            slider.setValue(0)
            slider.valueChanged.connect(lambda value, p=param: self.updateLabel(p, value))

            slider_layout.addWidget(label)
            slider_layout.addWidget(slider)

            vbox.addLayout(slider_layout)

            self.sliders[param] = slider
            self.labels[param] = label

        # Add a label for the preview display
        self.preview_label = QLabel(self)
        self.preview_label.setFixedSize(300, 200)  # Set size for the preview window
        vbox.addWidget(self.preview_label)

        # Add a button to copy the values to the clipboard
        copy_button = QPushButton('Copy to Clipboard', self)
        copy_button.clicked.connect(self.copyToClipboard)

        vbox.addWidget(copy_button)

        # Timer to refresh the preview area periodically
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updatePreview)
        self.timer.start(100)  # Update every 100 ms

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
        # coordinates = f'({x1}, {y1}), ({x2}, {y2})'
        coordinates = f'({x1}, {y1}, {x2}, {y2})'

        clipboard = QApplication.clipboard()
        clipboard.setText(coordinates)

        # Inform the user
        self.labels['X1'].setText(f'Copied: {coordinates}')

    def updatePreview(self):
        # Get the current slider values
        x1 = self.sliders['X1'].value()
        y1 = self.sliders['Y1'].value()
        x2 = self.sliders['X2'].value()
        y2 = self.sliders['Y2'].value()

        # Capture the part of the screen defined by the slider values
        if x2 > x1 and y2 > y1:
            screen_geom = self.screen.geometry()
            width = x2 - x1
            height = y2 - y1

            # Take screenshot of the selected region
            screenshot = self.screen.grabWindow(0, x1, y1, width, height)
            screenshot = screenshot.scaled(self.preview_label.size(), Qt.KeepAspectRatio)

            # Update the preview label with the captured image
            self.preview_label.setPixmap(screenshot)
        else:
            self.preview_label.clear()  # Clear the preview if invalid coordinates are given

# Main loop
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SearchWindowParameters()
    win.show()
    sys.exit(app.exec_())
