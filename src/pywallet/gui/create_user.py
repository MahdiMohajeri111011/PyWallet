import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class LoginView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyWallet - Sign In")
        self.setFixedSize(1200, 750)
        self.setStyleSheet("background-color: #0f172a;")
        self.init_ui()

    def init_ui(self):
        # Main layout
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(100, 70, 100, 70)
        main_layout.setSpacing(80)

        # =========================
        # Left Section
        # =========================
        left_widget = QWidget()
        left_widget.setFixedWidth(400)
        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignTop)

        # Logo
        logo = QLabel("₿")
        logo.setStyleSheet("""
            color: #38bdf8;
            font-size: 56px;
            font-weight: bold;
            font-family: Segoe UI;
        """)
        left_layout.addWidget(logo)
        left_layout.addSpacing(15)

        # Title
        title = QLabel("PyWallet")
        title.setStyleSheet("""
            color: white;
            font-size: 38px;
            font-weight: bold;
            font-family: Segoe UI;
        """)
        left_layout.addWidget(title)
        left_layout.addSpacing(20)

        # Subtitle
        subtitle = QLabel("Welcome back!\nSign in to your account.")
        subtitle.setStyleSheet("""
            color: #94a3b8;
            font-size: 16px;
            font-family: Segoe UI;
        """)
        subtitle.setWordWrap(True)
        left_layout.addWidget(subtitle)

        left_widget.setLayout(left_layout)

        # =========================
        # Right Card
        # =========================
        card = QWidget()
        card.setStyleSheet("""
            QWidget {
                background-color: #1e293b;
                border-radius: 15px;
            }
        """)
        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(50, 40, 50, 40)
        card_layout.setSpacing(10)

        # Header
        header = QLabel("Sign In")
        header.setStyleSheet("""
            color: white;
            font-size: 28px;
            font-weight: bold;
            font-family: Segoe UI;
        """)
        card_layout.addWidget(header)

        description = QLabel("Enter your credentials to access your wallet.")
        description.setStyleSheet("""
            color: #94a3b8;
            font-size: 14px;
            font-family: Segoe UI;
        """)
        card_layout.addWidget(description)
        card_layout.addSpacing(25)

        # Form
        form_widget = QWidget()
        form_layout = QVBoxLayout()
        form_layout.setSpacing(15)

        # Username
        username_label = QLabel("Username")
        username_label.setStyleSheet("""
            color: #cbd5e1;
            font-size: 13px;
            font-weight: bold;
            font-family: Segoe UI;
        """)
        form_layout.addWidget(username_label)
        self.username_entry = QLineEdit()
        self.username_entry.setStyleSheet("""
            QLineEdit {
                background-color: #2d3748;
                color: #e2e8f0;
                font-size: 16px;
                font-family: Segoe UI;
                padding: 14px;
                border: none;
                border-radius: 8px;
                min-height: 20px;
            }
        """)
        form_layout.addWidget(self.username_entry)

        # Password
        password_label = QLabel("Password")
        password_label.setStyleSheet("""
            color: #cbd5e1;
            font-size: 13px;
            font-weight: bold;
            font-family: Segoe UI;
        """)
        form_layout.addWidget(password_label)
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)
        self.password_entry.setStyleSheet("""
            QLineEdit {
                background-color: #2d3748;
                color: #e2e8f0;
                font-size: 16px;
                font-family: Segoe UI;
                padding: 14px;
                border: none;
                border-radius: 8px;
                min-height: 20px;
            }
        """)
        form_layout.addWidget(self.password_entry)

        form_widget.setLayout(form_layout)
        card_layout.addWidget(form_widget)
        card_layout.addSpacing(30)

        # =========================
        # Buttons
        # =========================

        # Sign In Button
        self.signin_btn = QPushButton("Sign In")
        self.signin_btn.setStyleSheet("""
            QPushButton {
                background-color: #0284c7;
                color: white;
                font-size: 16px;
                font-weight: bold;
                font-family: Segoe UI;
                padding: 16px;
                border: none;
                border-radius: 8px;
                min-height: 30px;
            }
            QPushButton:hover {
                background-color: #0369a1;
            }
        """)
        self.signin_btn.clicked.connect(self.sign_in)
        card_layout.addWidget(self.signin_btn)
        card_layout.addSpacing(15)

        # Go to Create Account Button
        self.goto_signup_btn = QPushButton("Create New Account")
        self.goto_signup_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #38bdf8;
                font-size: 14px;
                font-weight: bold;
                font-family: Segoe UI;
                padding: 14px;
                border: none;
            }
            QPushButton:hover {
                background-color: #2d3748;
                border-radius: 8px;
            }
        """)
        self.goto_signup_btn.clicked.connect(self.switch_to_signup)
        card_layout.addWidget(self.goto_signup_btn)

        card.setLayout(card_layout)

        # Add to main layout
        main_layout.addWidget(left_widget)
        main_layout.addWidget(card)

        self.setLayout(main_layout)

    def sign_in(self):
        username = self.username_entry.text()
        password = self.password_entry.text()

        if not username:
            QMessageBox.warning(self, "Error", "Username is required.")
            return

        if not password:
            QMessageBox.warning(self, "Error", "Password is required.")
            return

        print(f"Sign In - Username: {username}, Password: {password}")
        QMessageBox.information(self, "Success", f"Welcome back, {username}!")

    def switch_to_signup(self):
        self.close()
        self.create_account_window = CreateUserView()
        self.create_account_window.show()


class CreateUserView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyWallet - Create Account")
        self.setFixedSize(1200, 750)
        self.setStyleSheet("background-color: #0f172a;")
        self.init_ui()

    def init_ui(self):
        # Main layout
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(100, 70, 100, 70)
        main_layout.setSpacing(80)

        # =========================
        # Left Section
        # =========================
        left_widget = QWidget()
        left_widget.setFixedWidth(400)
        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignTop)

        # Logo
        logo = QLabel("₿")
        logo.setStyleSheet("""
            color: #38bdf8;
            font-size: 56px;
            font-weight: bold;
            font-family: Segoe UI;
        """)
        left_layout.addWidget(logo)
        left_layout.addSpacing(15)

        # Title
        title = QLabel("PyWallet")
        title.setStyleSheet("""
            color: white;
            font-size: 38px;
            font-weight: bold;
            font-family: Segoe UI;
        """)
        left_layout.addWidget(title)
        left_layout.addSpacing(20)

        # Subtitle
        subtitle = QLabel("Your simple and secure\nwallet management system.")
        subtitle.setStyleSheet("""
            color: #94a3b8;
            font-size: 16px;
            font-family: Segoe UI;
        """)
        subtitle.setWordWrap(True)
        left_layout.addWidget(subtitle)

        left_widget.setLayout(left_layout)

        # =========================
        # Right Card
        # =========================
        card = QWidget()
        card.setStyleSheet("""
            QWidget {
                background-color: #1e293b;
                border-radius: 15px;
            }
        """)
        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(50, 40, 50, 40)
        card_layout.setSpacing(8)

        # Header
        header = QLabel("Create your account")
        header.setStyleSheet("""
            color: white;
            font-size: 28px;
            font-weight: bold;
            font-family: Segoe UI;
        """)
        card_layout.addWidget(header)

        description = QLabel("Enter your information to get started.")
        description.setStyleSheet("""
            color: #94a3b8;
            font-size: 14px;
            font-family: Segoe UI;
        """)
        card_layout.addWidget(description)
        card_layout.addSpacing(20)

        # =========================
        # Form - Using Scroll Area for safety
        # =========================
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("""
            QScrollArea {
                background-color: transparent;
                border: none;
            }
            QScrollBar:vertical {
                background-color: #1e293b;
                width: 8px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical {
                background-color: #38bdf8;
                border-radius: 4px;
                min-height: 20px;
            }
        """)

        form_widget = QWidget()
        form_widget.setStyleSheet("background-color: transparent;")
        form_layout = QVBoxLayout()
        form_layout.setSpacing(12)
        form_layout.setContentsMargins(0, 0, 0, 0)

        # 1. Username
        username_label = QLabel("Username")
        username_label.setStyleSheet("""
            color: #cbd5e1;
            font-size: 13px;
            font-weight: bold;
            font-family: Segoe UI;
        """)
        form_layout.addWidget(username_label)
        self.username_entry = QLineEdit()
        self.username_entry.setStyleSheet("""
            QLineEdit {
                background-color: #2d3748;
                color: #e2e8f0;
                font-size: 16px;
                font-family: Segoe UI;
                padding: 14px;
                border: none;
                border-radius: 8px;
                min-height: 20px;
            }
        """)
        form_layout.addWidget(self.username_entry)

        # 2. Password
        password_label = QLabel("Password")
        password_label.setStyleSheet("""
            color: #cbd5e1;
            font-size: 13px;
            font-weight: bold;
            font-family: Segoe UI;
        """)
        form_layout.addWidget(password_label)
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)
        self.password_entry.setStyleSheet("""
            QLineEdit {
                background-color: #2d3748;
                color: #e2e8f0;
                font-size: 16px;
                font-family: Segoe UI;
                padding: 14px;
                border: none;
                border-radius: 8px;
                min-height: 20px;
            }
        """)
        form_layout.addWidget(self.password_entry)

        # 3. First Name + Last Name (Horizontal)
        name_label = QLabel("Full Name")
        name_label.setStyleSheet("""
            color: #cbd5e1;
            font-size: 13px;
            font-weight: bold;
            font-family: Segoe UI;
        """)
        form_layout.addWidget(name_label)

        name_layout = QHBoxLayout()
        name_layout.setSpacing(15)

        # First Name
        first_name_layout = QVBoxLayout()
        first_name_layout.setSpacing(5)
        first_name_label = QLabel("First name")
        first_name_label.setStyleSheet("""
            color: #94a3b8;
            font-size: 11px;
            font-family: Segoe UI;
        """)
        first_name_layout.addWidget(first_name_label)
        self.firstname_entry = QLineEdit()
        self.firstname_entry.setStyleSheet("""
            QLineEdit {
                background-color: #2d3748;
                color: #e2e8f0;
                font-size: 16px;
                font-family: Segoe UI;
                padding: 14px;
                border: none;
                border-radius: 8px;
                min-height: 20px;
            }
        """)
        first_name_layout.addWidget(self.firstname_entry)
        name_layout.addLayout(first_name_layout)

        # Last Name
        last_name_layout = QVBoxLayout()
        last_name_layout.setSpacing(5)
        last_name_label = QLabel("Last name")
        last_name_label.setStyleSheet("""
            color: #94a3b8;
            font-size: 11px;
            font-family: Segoe UI;
        """)
        last_name_layout.addWidget(last_name_label)
        self.lastname_entry = QLineEdit()
        self.lastname_entry.setStyleSheet("""
            QLineEdit {
                background-color: #2d3748;
                color: #e2e8f0;
                font-size: 16px;
                font-family: Segoe UI;
                padding: 14px;
                border: none;
                border-radius: 8px;
                min-height: 20px;
            }
        """)
        last_name_layout.addWidget(self.lastname_entry)
        name_layout.addLayout(last_name_layout)

        form_layout.addLayout(name_layout)

        # 4. Email
        email_label = QLabel("Email")
        email_label.setStyleSheet("""
            color: #cbd5e1;
            font-size: 13px;
            font-weight: bold;
            font-family: Segoe UI;
        """)
        form_layout.addWidget(email_label)
        self.email_entry = QLineEdit()
        self.email_entry.setStyleSheet("""
            QLineEdit {
                background-color: #2d3748;
                color: #e2e8f0;
                font-size: 16px;
                font-family: Segoe UI;
                padding: 14px;
                border: none;
                border-radius: 8px;
                min-height: 20px;
            }
        """)
        form_layout.addWidget(self.email_entry)

        # 5. Phone
        phone_label = QLabel("Phone number")
        phone_label.setStyleSheet("""
            color: #cbd5e1;
            font-size: 13px;
            font-weight: bold;
            font-family: Segoe UI;
        """)
        form_layout.addWidget(phone_label)
        self.phone_entry = QLineEdit()
        self.phone_entry.setStyleSheet("""
            QLineEdit {
                background-color: #2d3748;
                color: #e2e8f0;
                font-size: 16px;
                font-family: Segoe UI;
                padding: 14px;
                border: none;
                border-radius: 8px;
                min-height: 20px;
            }
        """)
        form_layout.addWidget(self.phone_entry)

        form_widget.setLayout(form_layout)
        scroll.setWidget(form_widget)
        card_layout.addWidget(scroll)

        # =========================
        # Buttons
        # =========================

        # Create Account Button
        self.create_btn = QPushButton("Create Account")
        self.create_btn.setStyleSheet("""
            QPushButton {
                background-color: #0284c7;
                color: white;
                font-size: 16px;
                font-weight: bold;
                font-family: Segoe UI;
                padding: 16px;
                border: none;
                border-radius: 8px;
                min-height: 30px;
            }
            QPushButton:hover {
                background-color: #0369a1;
            }
        """)
        self.create_btn.clicked.connect(self.create_user)
        card_layout.addWidget(self.create_btn)
        card_layout.addSpacing(10)

        # Go to Sign In Button
        self.goto_login_btn = QPushButton("Already have an account? Sign In")
        self.goto_login_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #38bdf8;
                font-size: 14px;
                font-weight: bold;
                font-family: Segoe UI;
                padding: 14px;
                border: none;
            }
            QPushButton:hover {
                background-color: #2d3748;
                border-radius: 8px;
            }
        """)
        self.goto_login_btn.clicked.connect(self.switch_to_login)
        card_layout.addWidget(self.goto_login_btn)

        card.setLayout(card_layout)

        # Add to main layout
        main_layout.addWidget(left_widget)
        main_layout.addWidget(card)

        self.setLayout(main_layout)

    def create_user(self):
        username = self.username_entry.text()
        password = self.password_entry.text()
        firstname = self.firstname_entry.text()
        lastname = self.lastname_entry.text()
        email = self.email_entry.text()
        phone = self.phone_entry.text()

        if not username:
            QMessageBox.warning(self, "Error", "Username is required.")
            return

        if not password:
            QMessageBox.warning(self, "Error", "Password is required.")
            return

        if len(password) < 6:
            QMessageBox.warning(self, "Error", "Password must be at least 6 characters.")
            return

        print("Username:", username)
        print("Password:", password)
        print("First name:", firstname)
        print("Last name:", lastname)
        print("Email:", email)
        print("Phone:", phone)

        QMessageBox.information(self, "Success", "Account created successfully!")
        self.switch_to_login()

    def switch_to_login(self):
        self.close()
        self.login_window = LoginView()
        self.login_window.show()

    def switch_to_signup(self):
        self.close()
        self.create_account_window = CreateUserView()
        self.create_account_window.show()


def main():
    app = QApplication(sys.argv)
    window = LoginView()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()