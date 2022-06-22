from PyQt5 import QtCore, QtGui, QtWidgets


class UiApplication(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(800, 435)
        Window.setStyleSheet("border: None;")
        Window.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(55, 60, 90);")

        """
        add hint-panel
        """
        self.hint = QtWidgets.QFrame(self.centralwidget)
        self.hint.setGeometry(0, 0, 802, 30)
        self.hint.setStyleSheet("background: rgb(55, 60, 90);")

        self.name_app = QtWidgets.QLabel(self.hint)
        self.name_app.setGeometry(20, 0, 100, 30)
        self.name_app.setText("Curiosity-Sign")
        self.name_app.setStyleSheet("QLabel {"
                                    "   color: rgb(250, 250, 250);"
                                    "}")

        self.close_button = QtWidgets.QPushButton(self.hint)
        self.close_button.setGeometry(770, 0, 30, 30)
        self.close_button.setStyleSheet("QPushButton:hover {"
                                        "   background: rgb(100, 10, 10);"
                                        "   border-radius: 10px;"
                                        "}"
                                        )
        self.close_button.setIcon(QtGui.QIcon("../style/close.png"))
        self.close_button.setIconSize(QtCore.QSize(20, 20))
        self.close_button.setObjectName("close")

        self.minimize_button = QtWidgets.QPushButton(self.hint)
        self.minimize_button.setGeometry(740, 0, 30, 30)
        self.minimize_button.setStyleSheet("QPushButton {"
                                           "}"
                                           "QPushButton:hover {"
                                           "   background: rgb(70, 70, 90);"
                                           "   border-radius: 10px;"
                                           "}"
                                           )
        self.minimize_button.setIcon(QtGui.QIcon('../style/minimize2.png'))
        self.minimize_button.setIconSize(QtCore.QSize(25, 25))
        self.minimize_button.setObjectName("minimize")

        """
        create areas with page
        """
        self.windows = QtWidgets.QTabWidget(self.centralwidget)
        self.windows.setEnabled(True)
        self.windows.setGeometry(QtCore.QRect(0, 30, 802, 437))
        self.windows.setStyleSheet("QTabBar::tab:hover {"
                                   "    background: rgb(100,100,100);"
                                   "    border-radius: 25px;"
                                   "}"
                                   "QTabBar::tab:selected {"
                                   "    background: rgb(250,250,250);"
                                   "    border-radius: 25px;"
                                   "}"
                                   "QTabBar::tab {"
                                   "    background: rgba(55, 59, 89, 0%);"
                                   "    height: 50px;"
                                   "    width: 50px;"
                                   "    border: none;"
                                   "    margin: 0px;"
                                   "    padding-top: -10px;"
                                   "    padding-bottom: 10px;"
                                   "    padding-left: 3px;"
                                   "}")
        self.windows.setTabPosition(QtWidgets.QTabWidget.West)
        self.windows.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.windows.setTabBarAutoHide(False)  # i can delete this string, but i don`t use this function
        self.windows.setObjectName("windows")

        """
        start page
        """
        self.home = QtWidgets.QWidget()
        self.home.setStyleSheet("QWidget {"
                                "    background-image: url('../style/space2.jpg');"
                                "    border: None;"
                                "}"
                                )
        self.home.setObjectName("home")
        self.windows.addTab(self.home, "")

        self.welcom_lable = QtWidgets.QLabel(self.home)
        self.welcom_lable.setText("Welcome to Curiosity-Sign")
        self.welcom_lable.setGeometry(75, 55, 600, 100)
        self.welcom_lable.setStyleSheet("QLabel {"
                                        "   background: rgba(100, 100, 100, 30%);"
                                        "   color: rgb(250, 250, 250);"
                                        "   font-size: 40px;"
                                        "   border-radius: 50px;"
                                        "}"
                                        )
        self.welcom_lable.setAlignment(QtCore.Qt.AlignCenter)

        self.short_info = QtWidgets.QLabel(self.home)
        self.short_info.setText("   This is a little program\n"
                                "   It will help you protect your information")
        self.short_info.setGeometry(115, 205, 520, 100)
        self.short_info.setStyleSheet("QLabel {"
                                      "   background: rgba(100, 100, 100, 30%);"
                                      "   color: rgb(250, 250, 250);"
                                      "   font-size: 25px;"
                                      "   border-radius: 25px;"
                                      "}"
                                      )

        self.created = QtWidgets.QLabel(self.home)
        self.created.setText("Created: BerlinerBY")
        self.created.setGeometry(600, 385, 140, 20)
        self.created.setStyleSheet("QLabel {"
                                   "   background: rgba(0, 0, 0, 0%);"
                                   "   color: rgb(250, 250, 250);"
                                   "   font-size: 15px;"
                                   "}"
                                   )

        """
        page where sign-algorithm start
        """

        style_qlineedit = str("QLineEdit {"
                              "    background-color: rgb(255, 170, 0);"
                              "    border-radius: 10px;"
                              "    font-size: 20px;"
                              "    padding-left: 10px;"
                              "}")
        style_button = str("QPushButton {"
                           "    border-radius: 20px;"
                           "    background-color: Transparent;"
                           "}"
                           "QPushButton:hover:!pressed {"
                           "    background: rgb(255, 170, 0);"
                           "}")

        trash_icon = QtGui.QIcon('../style/trash_icon.png')
        archive_icon = QtGui.QIcon('../style/archive_icon.png')

        self.input = QtWidgets.QWidget()
        self.input.setStyleSheet("QWidget {"
                                 "    background-color: #3d4fa1;"  # rgb(35, 40, 70)
                                 "}")
        self.input.setObjectName("input")
        self.windows.addTab(self.input, "")

        self.sign_path_to_container = QtWidgets.QLineEdit(self.input)
        self.sign_path_to_container.setGeometry(30, 30, 590, 55)
        self.sign_path_to_container.setPlaceholderText("Please enter path to DOCX file...")
        self.sign_path_to_container.setStyleSheet(style_qlineedit)
        self.sign_path_to_container.setObjectName("sign_path_to_container")

        self.sign_clear_path = QtWidgets.QPushButton(self.input)
        self.sign_clear_path.setGeometry(QtCore.QRect(625, 30, 45, 55))
        self.sign_clear_path.setStyleSheet(style_button)
        self.sign_clear_path.setIcon(trash_icon)
        self.sign_clear_path.setIconSize(QtCore.QSize(45, 55))
        self.sign_clear_path.setObjectName("sign_clear_path ")

        self.sign_open_container = QtWidgets.QPushButton(self.input)
        self.sign_open_container.setGeometry(QtCore.QRect(675, 30, 45, 55))
        self.sign_open_container.setStyleSheet(style_button)
        self.sign_open_container.setIcon(archive_icon)
        self.sign_open_container.setIconSize(QtCore.QSize(45, 55))
        self.sign_open_container.setObjectName("sign_open_container")

        self.sign_button = QtWidgets.QPushButton(self.input)
        self.sign_button.setGeometry(QtCore.QRect(275, 120, 200, 60))
        self.sign_button.setStyleSheet("QPushButton {"
                                       "    background: #68799e;"
                                       "    font-size: 20px;"
                                       "    border-radius: 15px;"
                                       "    font-size: 25px;"
                                       "}"
                                       "QPushButton:hover:!pressed {"
                                       "    background-color: rgb(55, 60, 90);"
                                       "}")
        self.sign_button.setText("Sign")
        self.sign_button.setIcon(QtGui.QIcon('../style/hide_icon.png'))
        self.sign_button.setIconSize(QtCore.QSize(20, 20))
        self.sign_button.setObjectName("sign")

        # подключить панель прогресса
        self.sign_progress = QtWidgets.QProgressBar(self.input)
        self.sign_progress.setGeometry(30, 215, 690, 60)
        self.sign_progress.setMaximum(100)
        self.sign_progress.setStyleSheet("QProgressBar {"
                                         "  background: #6a839c;"
                                         "  border-radius: 15px;"
                                         "  color: black;"
                                         "  text-align: center;"
                                         "  font-size: 20px;"
                                         "}"
                                         "QProgressBar::chunk {"
                                         "  background-color: #69babf;"
                                         "  border-radius :15px;"
                                         "}")
        self.sign_progress.setObjectName("sign_progress")

        self.sign_notifications = QtWidgets.QTextEdit(self.input)
        self.sign_notifications.setGeometry(QtCore.QRect(30, 310, 690, 60))
        self.sign_notifications.setStyleSheet("QTextEdit {"
                                              "    background-color: rgb(255, 255, 255);"
                                              "    border-radius: 15px;"
                                              "    font-size: 20px;"
                                              "    padding-top: 12px;"
                                              "    padding-left: 10px;"
                                              "}")
        self.sign_notifications.setObjectName("sign_notifications")
        self.sign_notifications.setAlignment(QtCore.Qt.AlignCenter)

        """
        page where verification-algorithm start
        """
        self.output = QtWidgets.QWidget()
        self.output.setStyleSheet("QWidget {"
                                  "    background-color: #3d4fa1;"
                                  "}")
        self.output.setObjectName("output")
        self.windows.addTab(self.output, "")

        """адрес контейнера"""
        self.verification_path_to_container = QtWidgets.QLineEdit(self.output)
        self.verification_path_to_container.setGeometry(QtCore.QRect(30, 30, 590, 45))
        self.verification_path_to_container.setStyleSheet(style_qlineedit)
        self.verification_path_to_container.setObjectName("verification_path_to_container")
        self.verification_path_to_container.setPlaceholderText("Please enter path to DOCX file...")

        """кнопка отчистки адреса контейнера"""
        self.verification_clear_path = QtWidgets.QPushButton(self.output)
        self.verification_clear_path.setGeometry(QtCore.QRect(625, 30, 45, 45))
        self.verification_clear_path.setStyleSheet(style_button)
        self.verification_clear_path.setIcon(trash_icon)
        self.verification_clear_path.setIconSize(QtCore.QSize(45, 45))
        self.verification_clear_path.setObjectName("verification_clear_path")

        """кнопка открывающая мои документы для автоматического выбора файла"""
        self.verification_open_container = QtWidgets.QPushButton(self.output)
        self.verification_open_container.setGeometry(QtCore.QRect(675, 30, 45, 45))
        self.verification_open_container.setStyleSheet(style_button)
        self.verification_open_container.setIcon(archive_icon)
        self.verification_open_container.setIconSize(QtCore.QSize(45, 45))
        self.verification_open_container.setObjectName("verification_open_container")

        """поле для ввода ключа RSA"""
        self.verification_RSA_key = QtWidgets.QLineEdit(self.output)
        self.verification_RSA_key.setGeometry(QtCore.QRect(30, 105, 590, 45))
        self.verification_RSA_key.setStyleSheet(style_qlineedit)
        self.verification_RSA_key.setObjectName("verification_RSA_key")
        self.verification_RSA_key.setPlaceholderText("Please enter verification key...")

        """кнопка для отчистки поля с ключом RSA"""
        self.verification_clear_RSA_key = QtWidgets.QPushButton(self.output)
        self.verification_clear_RSA_key.setGeometry(QtCore.QRect(625, 105, 95, 45))
        self.verification_clear_RSA_key.setStyleSheet(style_button)
        self.verification_clear_RSA_key.setIcon(trash_icon)
        self.verification_clear_RSA_key.setIconSize(QtCore.QSize(45, 45))
        self.verification_clear_RSA_key.setObjectName("verification_clear_RSA_key")

        """кнопка для запуска алгоритма"""
        self.verification_Button = QtWidgets.QPushButton(self.output)
        self.verification_Button.setGeometry(QtCore.QRect(275, 180, 200, 45))
        self.verification_Button.setStyleSheet("QPushButton {"
                                               "    background: #68799e;"
                                               "    font-size: 20px;"
                                               "    border-radius: 15px;"
                                               "    font-size: 25px;"
                                               "}"
                                               "QPushButton:hover:!pressed {"
                                               "    background-color: rgb(55, 60, 90);"
                                               "}")
        self.verification_Button.setObjectName("verification_Button")

        self.verification_progress = QtWidgets.QProgressBar(self.output)
        self.verification_progress.setGeometry(30, 260, 690, 45)
        self.verification_progress.setMaximum(100)
        self.verification_progress.setStyleSheet("QProgressBar {"
                                                 "  background: #6a839c;"
                                                 "  border-radius: 15px;"
                                                 "  color: black;"
                                                 "  text-align: center;"
                                                 "  font-size: 20px;"
                                                 "}"
                                                 "QProgressBar::chunk {"
                                                 "  background-color: #69babf;"
                                                 "  border-radius :15px;"
                                                 "}")
        self.verification_progress.setObjectName("verification_progress")

        self.verification_notification = QtWidgets.QTextEdit(self.output)
        self.verification_notification.setGeometry(QtCore.QRect(30, 335, 690, 45))
        self.verification_notification.setStyleSheet("QTextEdit {"
                                                     "    background-color: rgb(255, 255, 255);"
                                                     "    border-radius: 15px;"
                                                     "    font-size: 20px;"
                                                     "    padding-top: 6px;"
                                                     "    padding-left: 10px;"
                                                     "}")
        self.verification_notification.setObjectName("verification_notification")
        self.verification_notification.setAlignment(QtCore.Qt.AlignCenter)

        """
        page with help-info
        """
        self.support = QtWidgets.QWidget()
        self.support.setStyleSheet("QWidget {"
                                   "    background-color: #3d4fa1;"
                                   "}")
        self.support.setObjectName("support")
        self.windows.addTab(self.support, "")

        self.key_info = QtWidgets.QLabel(self.support)
        self.key_info.setText("Your public key for verification")
        self.key_info.setGeometry(45, 45, 660, 100)
        self.key_info.setStyleSheet("QLabel {"
                                    "   background: #6a839c;"
                                    "   color: rgb(0, 0, 0);"
                                    "   font-size: 20px;"
                                    "   border-radius: 25px;"
                                    "}"
                                    )
        self.key_info.setAlignment(QtCore.Qt.AlignHCenter)


        self.key = QtWidgets.QTextEdit(self.key_info)
        self.key.setGeometry(QtCore.QRect(30, 30, 600, 45))
        self.key.setStyleSheet("QTextEdit {"
                               "    background-color: rgb(255, 255, 255);"
                               "    border-radius: 15px;"
                               "    font-size: 20px;"
                               "    padding-top: 6px;"
                               "    padding-left: 10px;"
                               "}")
        self.key.setObjectName("key")
        self.key.setReadOnly(True)

        self.windows.setTabIcon(0, QtGui.QIcon('../style/home2.png'))
        self.windows.setTabIcon(1, QtGui.QIcon('../style/input.png'))
        self.windows.setTabIcon(2, QtGui.QIcon('../style/output.png'))
        self.windows.setTabIcon(3, QtGui.QIcon('../style/information.png'))
        self.windows.setIconSize(QtCore.QSize(30, 35))

        Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window)
        self.windows.setCurrentIndex(0)  # не забыть поставить в конце работы 0
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Curiosity-sign"))

        self.verification_Button.setText(_translate("Window", "Verification"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = UiApplication()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())
