import base64
import sys
from pathlib import Path

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

SALT_SIZE = 16


def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=390_000)
    return base64.urlsafe_b64encode(kdf.derive(password.encode("utf-8")))


class DropArea(QLabel):
    def __init__(self, parent=None):
        super().__init__("Drag a file here to decrypt", parent)
        self.setAlignment(Qt.AlignCenter)
        self.setAcceptDrops(True)
        self.setMinimumHeight(60)
        self.setStyleSheet(
            "border: 2px dashed gray; border-radius: 6px; color: gray;"
        )
        self.file_path: Path | None = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if not urls:
            return
        self.file_path = Path(urls[0].toLocalFile())
        self.setText(self.file_path.name)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Encrypt / Decrypt")
        self.setGeometry(100, 100, 500, 500)

        central = QWidget(self)
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        self.drop_area = DropArea(self)
        layout.addWidget(self.drop_area)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.decrypt_button = QPushButton("Decrypt Dropped File", self)
        self.decrypt_button.clicked.connect(self.decrypt_file)
        layout.addWidget(self.decrypt_button)

        self.text_edit = QTextEdit(self)
        layout.addWidget(self.text_edit)

        self.export_button = QPushButton("Encrypt && Export", self)
        self.export_button.clicked.connect(self.encrypt_and_export)
        layout.addWidget(self.export_button)

    def decrypt_file(self):
        if self.drop_area.file_path is None:
            QMessageBox.warning(self, "No file", "Drag a file into the box first.")
            return

        password = self.password_input.text()
        if not password:
            QMessageBox.warning(self, "No password", "Enter the password first.")
            return

        try:
            data = self.drop_area.file_path.read_bytes()
            salt, token = data[:SALT_SIZE], data[SALT_SIZE:]
            key = derive_key(password, salt)
            plaintext = Fernet(key).decrypt(token)
        except InvalidToken:
            QMessageBox.critical(self, "Decryption failed", "Wrong password or corrupt file.")
            return
        except OSError as exc:
            QMessageBox.critical(self, "Decryption failed", str(exc))
            return

        self.text_edit.setPlainText(plaintext.decode("utf-8"))

    def encrypt_and_export(self):
        password = self.password_input.text()
        if not password:
            QMessageBox.warning(self, "No password", "Enter a password first.")
            return

        save_path, _ = QFileDialog.getSaveFileName(self, "Export Encrypted File")
        if not save_path:
            return

        salt = Fernet.generate_key()[:SALT_SIZE]
        key = derive_key(password, salt)
        token = Fernet(key).encrypt(self.text_edit.toPlainText().encode("utf-8"))
        Path(save_path).write_bytes(salt + token)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
