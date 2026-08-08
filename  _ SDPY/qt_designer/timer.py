import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton
)
from PyQt5.QtCore import QTimer, Qt

WARN_AT_SECONDS_LEFT = 30

PRESETS = {
    "Speaker (5 min)": 5 * 60,
    "Interviewer (3 min)": 3 * 60,
}


class CountdownTimer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SDPY - Talk Timer")
        self.resize(360, 220)

        self.total_seconds = 0
        self.seconds_left = 0
        self.warned = False

        self.tick = QTimer(self)
        self.tick.setInterval(1000)
        self.tick.timeout.connect(self.on_tick)

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        # Preset buttons
        preset_row = QHBoxLayout()
        for label, seconds in PRESETS.items():
            btn = QPushButton(label)
            btn.clicked.connect(lambda _, s=seconds: self.load_preset(s))
            preset_row.addWidget(btn)
        layout.addLayout(preset_row)

        # Big countdown display
        self.display = QLabel("00:00")
        self.display.setAlignment(Qt.AlignCenter)
        self.display.setStyleSheet("font-size: 64px; font-weight: bold;")
        layout.addWidget(self.display)

        # Controls
        control_row = QHBoxLayout()
        self.start_btn = QPushButton("Start")
        self.start_btn.clicked.connect(self.start)
        self.pause_btn = QPushButton("Pause")
        self.pause_btn.clicked.connect(self.pause)
        self.reset_btn = QPushButton("Reset")
        self.reset_btn.clicked.connect(self.reset)
        for w in (self.start_btn, self.pause_btn, self.reset_btn):
            control_row.addWidget(w)
        layout.addLayout(control_row)

        self.load_preset(PRESETS["Speaker (5 min)"])

    def load_preset(self, seconds):
        self.tick.stop()
        self.total_seconds = seconds
        self.seconds_left = seconds
        self.warned = False
        self.update_display()

    def start(self):
        if self.seconds_left > 0:
            self.tick.start()

    def pause(self):
        self.tick.stop()

    def reset(self):
        self.load_preset(self.total_seconds)

    def on_tick(self):
        self.seconds_left -= 1
        self.update_display()

        if self.seconds_left == WARN_AT_SECONDS_LEFT:
            self.warned = True
            QApplication.beep()

        if self.seconds_left <= 0:
            self.tick.stop()
            QApplication.beep()

    def update_display(self):
        minutes, seconds = divmod(max(self.seconds_left, 0), 60)
        self.display.setText(f"{minutes:02d}:{seconds:02d}")
        if self.seconds_left <= WARN_AT_SECONDS_LEFT and self.seconds_left > 0:
            self.display.setStyleSheet("font-size: 64px; font-weight: bold; color: red;")
        else:
            self.display.setStyleSheet("font-size: 64px; font-weight: bold;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CountdownTimer()
    window.show()
    sys.exit(app.exec_())
