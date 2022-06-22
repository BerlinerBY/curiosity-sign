import json
import sys
from PyQt5 import QtCore, QtWidgets
import carcass
from core.signing import write_hash_to_image
from core.verification import extract_hash_from_image


class AppCore(QtWidgets.QMainWindow, carcass.UiApplication):
    def __init__(self):
        super(AppCore, self).__init__()
        self.ui = carcass.UiApplication()
        self.ui.setupUi(self)

        self.ui.close_button.clicked.connect(lambda: self.close_window())
        self.ui.minimize_button.clicked.connect(lambda: self.minimize_window())

        self.ui.key.setText(load_public_key())
        self.ui.key.setAlignment(QtCore.Qt.AlignCenter)

        self.oldPos = self.pos()

        # buttons of clear line
        self.ui.sign_clear_path.clicked.connect(lambda: self.clear_sign_path_to_container())
        self.ui.verification_clear_path.clicked.connect(lambda: self.clear_verification_path_to_container())
        self.ui.verification_clear_RSA_key.clicked.connect(lambda: self.clear_verification_rsa_key())

        # buttons of file-dialog
        self.ui.sign_open_container.clicked.connect(lambda: self.sign_open_container())
        self.ui.verification_open_container.clicked.connect(lambda: self.verification_open_container())

        # buttons of run script
        self.ui.sign_button.clicked.connect(lambda: self.start_signing())
        self.ui.verification_Button.clicked.connect(lambda: self.start_verification())

    def start_signing(self):
        self.ui.sign_notifications.clear()
        self.sign_worker = write_hash_to_image.SignScript(self.ui.sign_path_to_container.text())
        self.sign_worker.count_percent.connect(self.on_sign_count_percent)
        self.sign_worker.sign_notification.connect(self.print_sign_notifications)

        self.sign_worker.start()

        self.ui.sign_path_to_container.clear()

    def on_sign_count_percent(self, value):
        self.ui.sign_progress.setValue(value)

    def print_sign_notifications(self, value):
        self.ui.sign_notifications.setText(value)

    def start_verification(self):
        self.ui.verification_notification.clear()
        self.verification_worker = extract_hash_from_image.VerificationScript(
            self.ui.verification_path_to_container.text(),
            self.ui.verification_RSA_key.text())

        self.verification_worker.count_percent.connect(self.on_verification_count_percent)
        self.verification_worker.global_finish.connect(self.print_verification_notification)
        self.verification_worker.start()

        self.ui.sign_path_to_container.clear()
        self.ui.verification_RSA_key.clear()

    def on_verification_count_percent(self, value):
        self.ui.verification_progress.setValue(value)

    def print_verification_notification(self, value):
        self.ui.verification_notification.setText(value)

    def sign_open_container(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Find file", "", "Text document(*.docx)",
                                                             options=options)
        if file_path:
            self.ui.sign_path_to_container.setText(file_path)

    def verification_open_container(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Find container", "", "Text Files(*.docx)",
                                                             options=options)
        if file_path:
            self.ui.verification_path_to_container.setText(file_path)

    def clear_sign_path_to_container(self):
        self.ui.sign_path_to_container.clear()

    def clear_verification_path_to_container(self):
        self.ui.verification_path_to_container.clear()

    def clear_verification_rsa_key(self):
        self.ui.verification_RSA_key.clear()

    def close_window(self):
        self.close()

    def minimize_window(self):
        self.showMinimized()

    def mousePressEvent(self, event):  # functions for move window
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):  # -//-
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


def load_public_key():
    with open('/home/berlinerby/PycharmProjects/curiosity-sign/core/rsa/key.json', 'r') as file:
        data = json.load(file)
        key = data.get('public_key')

    return key


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = AppCore()
    application.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
