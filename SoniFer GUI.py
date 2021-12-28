import sys
import PyQt6.QtCore as QtCore
import PyQt6.QtGui as QtGui
import PyQt6.QtWidgets as QtWidgets
from qt_material import apply_stylesheet
import Chatbot


def train_trevor():
    splash = QtWidgets.QSplashScreen()
    pix = QtGui.QPixmap('Logo.jpeg')
    splash.setPixmap(pix)
    splash.show()

    Chatbot.train_bot()

    splash.close()


def display_text(text, color, message_layout: QtWidgets.QVBoxLayout, alignment: QtCore.Qt.AlignmentFlag):
    new_text = ''  # for fixing an issue with warping text without whitespaces. \u200a is zero width whitespace

    if len(text) < 60:
        new_text = text
    else:
        for i in range(len(text) // 60):
            new_text += text[60 * (i - 1): 60 * i] + '\u200a'

    message = QtWidgets.QLabel(new_text.strip('\n'))
    message.setAlignment(alignment)
    message.setStyleSheet(f'color: {color};')
    message.setMinimumHeight(50)
    message.setWordWrap(True)
    message_layout.addWidget(message)


def clicked_send(textbox: QtWidgets.QTextEdit, message_layout: QtWidgets.QVBoxLayout):
    if ((text := textbox.toPlainText()).strip()).strip('\n'):
        display_text(text, 'white', message_layout, QtCore.Qt.AlignmentFlag.AlignLeft)
        textbox.clear()
        response = Chatbot.get_bot_response(text)
        display_text(str(response), 'green', message_layout, QtCore.Qt.AlignmentFlag.AlignRight)


class App(QtWidgets.QWidget):
    def __init__(self):
        super(App, self).__init__()

        self.NAME = "Son 'i' Fer"
        
        self.setWindowIcon(QtGui.QIcon("Logo.jpeg"))
        self.setWindowTitle(self.NAME)

        train_trevor()
        self.init()

    def init(self):
        self.setFixedSize(600, 450)
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        title = QtWidgets.QLabel()
        pix = QtGui.QPixmap('Logo.jpeg')
        title.setPixmap(pix.scaled(100, 100, QtCore.Qt.AspectRatioMode.KeepAspectRatio))
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        layout.addWidget(title)

        info_layout = QtWidgets.QHBoxLayout()
        layout.addLayout(info_layout)

        you_label = QtWidgets.QLabel('YOU')
        you_label.setStyleSheet('font-size: 16px;')
        you_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        info_layout.addWidget(you_label)

        bot_label = QtWidgets.QLabel('TREVOR')
        bot_label.setStyleSheet('font-size: 16px;')
        bot_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        info_layout.addWidget(bot_label)

        message_area = QtWidgets.QScrollArea()
        message_area.setStyleSheet('background-color: black;')
        message_widget = QtWidgets.QWidget()
        message_layout = QtWidgets.QVBoxLayout()
        message_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        message_widget.setLayout(message_layout)
        message_area.setWidgetResizable(True)
        message_area.setWidget(message_widget)
        layout.addWidget(message_area)

        send_layout = QtWidgets.QHBoxLayout()
        layout.addLayout(send_layout)

        typing_area = QtWidgets.QTextEdit()

        typing_area.setFixedHeight(70)

        send_layout.addWidget(typing_area)

        send_button = QtWidgets.QPushButton()
        send_button.clicked.connect(lambda: clicked_send(typing_area, message_layout))
        send_button.setIcon(QtGui.QIcon('Send_logo.png'))
        send_button.setIconSize(QtCore.QSize(90, 90))
        send_button.setFixedSize(70, 70)
        send_layout.addWidget(send_button)

        self.show()


if __name__ == '__main__':
    mainApp = QtWidgets.QApplication(sys.argv)
    mainApp.setStyle("Fusion")
    apply_stylesheet(mainApp, theme='my_dark_theme.xml')
    app = App()
    sys.exit(mainApp.exec())
