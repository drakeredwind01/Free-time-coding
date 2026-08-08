import sys
from pathlib import Path
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QSpinBox
)
from PyQt5.QtCore import QTimer, Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

DEFAULT_WARN_AT_SECONDS_LEFT = 30

PRESETS = {
    "Speaker (5 min)": 5 * 60,
    "Interviewer (3 min)": 3 * 60,
}

HERE = Path(__file__).resolve().parent
SOUNDS = HERE / "sounds" / "trimmed"

# Filenames are as specified, not a mislabel: the "end_3" bowl is used for the
# warning cue and the "warn_2" bowl is used for the ending cue.
WARNING_SOUND_PATH = SOUNDS / "warn_2_horst_neptun_solo_trim4s.mp3"
END_SOUND_PATH = SOUNDS / "end_3_cabled_mess_03_trim4s.mp3"

# 0-100, easy to tweak per sound
WARNING_VOLUME = 280
END_VOLUME = 300


class CountdownTimer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SDPY - Talk Timer (editable)")
        self.resize(360, 280)

        self.total_seconds = 0
        self.seconds_left = 0
        self.warned = False

        self.tick = QTimer(self)
        self.tick.setInterval(1000)
        self.tick.timeout.connect(self.on_tick)

        self.warning_player = QMediaPlayer(self)
        self.warning_player.setMedia(QMediaContent(QUrl.fromLocalFile(str(WARNING_SOUND_PATH))))
        self.warning_player.setVolume(WARNING_VOLUME)

        self.end_player = QMediaPlayer(self)
        self.end_player.setMedia(QMediaContent(QUrl.fromLocalFile(str(END_SOUND_PATH))))
        self.end_player.setVolume(END_VOLUME)

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

        # Editable total time (for edge cases outside the two presets)
        time_row = QHBoxLayout()
        time_row.addWidget(QLabel("Minutes:"))
        self.minutes_input = QSpinBox()
        self.minutes_input.setRange(0, 180)
        self.minutes_input.valueChanged.connect(self.sync_from_inputs)
        time_row.addWidget(self.minutes_input)
        time_row.addWidget(QLabel("Seconds:"))
        self.seconds_input = QSpinBox()
        self.seconds_input.setRange(0, 59)
        self.seconds_input.valueChanged.connect(self.sync_from_inputs)
        time_row.addWidget(self.seconds_input)
        layout.addLayout(time_row)

        # Editable warning threshold (for edge cases like a 10s lightning round)
        warn_row = QHBoxLayout()
        warn_row.addWidget(QLabel("Warn at (sec left):"))
        self.warn_input = QSpinBox()
        self.warn_input.setRange(0, 3600)
        self.warn_input.setValue(DEFAULT_WARN_AT_SECONDS_LEFT)
        self.warn_input.valueChanged.connect(self.update_display)
        warn_row.addWidget(self.warn_input)
        layout.addLayout(warn_row)

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
        minutes, secs = divmod(seconds, 60)
        self.minutes_input.setValue(minutes)
        self.seconds_input.setValue(secs)
        self.sync_from_inputs()

    def sync_from_inputs(self):
        # Total time is only editable while stopped; the spinboxes are
        # disabled during a run, so this only fires between runs.
        if self.tick.isActive():
            return
        self.total_seconds = self.minutes_input.value() * 60 + self.seconds_input.value()
        self.seconds_left = self.total_seconds
        self.warned = False
        self.update_display()

    def start(self):
        if self.seconds_left > 0:
            self.tick.start()
            self.minutes_input.setEnabled(False)
            self.seconds_input.setEnabled(False)

    def pause(self):
        self.tick.stop()
        self.minutes_input.setEnabled(True)
        self.seconds_input.setEnabled(True)

    def reset(self):
        self.tick.stop()
        self.minutes_input.setEnabled(True)
        self.seconds_input.setEnabled(True)
        self.sync_from_inputs()

    def on_tick(self):
        self.seconds_left -= 1
        self.update_display()

        warn_at = self.warn_input.value()
        if warn_at > 0 and self.seconds_left == warn_at:
            self.warned = True
            self.warning_player.play()

        if self.seconds_left <= 0:
            self.tick.stop()
            self.minutes_input.setEnabled(True)
            self.seconds_input.setEnabled(True)
            self.end_player.play()

    def update_display(self):
        minutes, seconds = divmod(max(self.seconds_left, 0), 60)
        self.display.setText(f"{minutes:02d}:{seconds:02d}")
        warn_at = self.warn_input.value()
        if 0 < self.seconds_left <= warn_at:
            self.display.setStyleSheet("font-size: 64px; font-weight: bold; color: red;")
        else:
            self.display.setStyleSheet("font-size: 64px; font-weight: bold;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CountdownTimer()
    window.show()
    sys.exit(app.exec_())
