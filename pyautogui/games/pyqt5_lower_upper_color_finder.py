import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider, QHBoxLayout, QVBoxLayout, QPushButton, QFrame
from PyQt5.QtCore import Qt
import numpy as np
import pyperclip
from PyQt5.QtGui import QColor

class HSVColorPicker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HSV Color Picker")

        # Create a preview frame
        self.preview_frame = QFrame()
        self.preview_frame.setFrameShape(QFrame.StyledPanel)
        self.preview_frame.setFrameShadow(QFrame.Raised)

        # ... (rest of your code)

        # Update the preview frame when slider values change
        self.upper_h_slider.valueChanged.connect(self.update_preview)
        self.upper_s_slider.valueChanged.connect(self.update_preview)
        self.upper_v_slider.valueChanged.connect(self.update_preview)
        self.lower_h_slider.valueChanged.connect(self.update_preview)
        self.lower_s_slider.valueChanged.connect(self.update_preview)
        self.lower_v_slider.valueChanged.connect(self.update_preview)

        # ... (rest of your code)

    def update_preview(self):
        upper_color = np.array([self.upper_h_slider.value(),
                                self.upper_s_slider.value(),
                                self.upper_v_slider.value()])
        lower_color = np.array([self.lower_h_slider.value(),
                                self.lower_s_slider.value(),
                                self.lower_v_slider.value()])

        # Create a gradient from lower to upper color
        gradient = np.linspace(lower_color, upper_color, 256, dtype=np.uint8)
        gradient_image = np.ones((20, 256, 3), dtype=np.uint8) * 255
        gradient_image[:, :, :] = gradient

        # Convert to QImage and display in the preview frame
        qimg = QImage(gradient_image.data, gradient_image.shape[1], gradient_image.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg)
        self.preview_frame.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HSVColorPicker()
    window.show()
    sys.exit(app.exec_())