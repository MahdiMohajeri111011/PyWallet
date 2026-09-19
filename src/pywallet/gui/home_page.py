from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QGraphicsOpacityEffect,
    QSizePolicy,
)
from PyQt5.QtCore import (
    Qt,
    QPropertyAnimation,
    QEasingCurve,
    QTimer,
    pyqtSignal,
)
from PyQt5.QtGui import QFont


class AnimatedButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

        self.setCursor(Qt.PointingHandCursor)

        self.setStyleSheet("""
            QPushButton {
                background-color: #1e293b;
                color: #e2e8f0;
                border: 1px solid #334155;
                border-radius: 12px;
                padding: 16px;
                font-size: 15px;
                font-weight: bold;
                text-align: left;
            }

            QPushButton:hover {
                background-color: #26364d;
                border: 1px solid #38bdf8;
                color: white;
            }

            QPushButton:pressed {
                background-color: #0f3b55;
            }
        """)

        self.animation = QPropertyAnimation(self, b"minimumHeight")
        self.animation.setDuration(120)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)

    def enterEvent(self, event):
        self.animation.stop()
        self.animation.setStartValue(self.height())
        self.animation.setEndValue(self.height() + 3)
        self.animation.start()

        super().enterEvent(event)

    def leaveEvent(self, event):
        self.animation.stop()
        self.animation.setStartValue(self.height())
        self.animation.setEndValue(max(50, self.height() - 3))
        self.animation.start()

        super().leaveEvent(event)


class HomePage(QWidget):

    logout_requested = pyqtSignal()

    def __init__(self, username):
        super().__init__()

        self.username = username
        self.balance = 0.00

        self.setWindowTitle("PyWallet")
        self.setFixedSize(1200, 750)

        self.setStyleSheet("""
            QWidget {
                background-color: #0f172a;
                color: #e2e8f0;
                font-family: Segoe UI;
            }
        """)

        self.setup_ui()

        # Fade-in animation
        self.fade_in()

    # ==========================================================
    # UI
    # ==========================================================

    def setup_ui(self):

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(25)

        # ======================================================
        # SIDEBAR
        # ======================================================

        sidebar = QFrame()
        sidebar.setFixedWidth(220)

        sidebar.setStyleSheet("""
            QFrame {
                background-color: #1e293b;
                border-radius: 18px;
            }
        """)

        sidebar_layout = QVBoxLayout()
        sidebar_layout.setContentsMargins(20, 25, 20, 25)
        sidebar_layout.setSpacing(12)

        # Logo
        logo = QLabel("₿")
        logo.setAlignment(Qt.AlignCenter)
        logo.setStyleSheet("""
            color: #38bdf8;
            font-size: 52px;
            font-weight: bold;
        """)

        sidebar_layout.addWidget(logo)

        # App name
        app_name = QLabel("PyWallet")
        app_name.setAlignment(Qt.AlignCenter)
        app_name.setStyleSheet("""
            color: white;
            font-size: 24px;
            font-weight: bold;
        """)

        sidebar_layout.addWidget(app_name)
        sidebar_layout.addSpacing(30)

        # Navigation
        self.dashboard_btn = self.create_sidebar_button(
            "⌂   Dashboard"
        )

        self.balance_btn = self.create_sidebar_button(
            "◈   Balance"
        )

        self.transactions_btn = self.create_sidebar_button(
            "↻   Transactions"
        )

        self.settings_btn = self.create_sidebar_button(
            "⚙   Settings"
        )

        sidebar_layout.addWidget(self.dashboard_btn)
        sidebar_layout.addWidget(self.balance_btn)
        sidebar_layout.addWidget(self.transactions_btn)
        sidebar_layout.addWidget(self.settings_btn)

        sidebar_layout.addStretch()

        # User section
        user_card = QFrame()
        user_card.setStyleSheet("""
            QFrame {
                background-color: #162235;
                border-radius: 12px;
            }
        """)

        user_layout = QVBoxLayout()
        user_layout.setContentsMargins(12, 12, 12, 12)

        user_label = QLabel("SIGNED IN AS")
        user_label.setStyleSheet("""
            color: #64748b;
            font-size: 10px;
            font-weight: bold;
        """)

        username_label = QLabel(self.username)
        username_label.setStyleSheet("""
            color: white;
            font-size: 14px;
            font-weight: bold;
        """)

        user_layout.addWidget(user_label)
        user_layout.addWidget(username_label)

        user_card.setLayout(user_layout)

        sidebar_layout.addWidget(user_card)
        sidebar_layout.addSpacing(10)

        # Logout
        logout_button = QPushButton("⇥   Logout")
        logout_button.setCursor(Qt.PointingHandCursor)

        logout_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #f87171;
                border: none;
                padding: 12px;
                font-size: 14px;
                font-weight: bold;
                text-align: left;
            }

            QPushButton:hover {
                background-color: #3b2025;
                border-radius: 8px;
            }
        """)

        logout_button.clicked.connect(self.logout)

        sidebar_layout.addWidget(logout_button)

        sidebar.setLayout(sidebar_layout)

        # ======================================================
        # MAIN CONTENT
        # ======================================================

        content = QWidget()

        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(5, 5, 5, 5)
        content_layout.setSpacing(20)

        # ------------------------------------------------------
        # Header
        # ------------------------------------------------------

        header_layout = QHBoxLayout()

        header_text_layout = QVBoxLayout()

        greeting = QLabel(
            f"Welcome back, {self.username} 👋"
        )

        greeting.setStyleSheet("""
            color: white;
            font-size: 28px;
            font-weight: bold;
        """)

        subtitle = QLabel(
            "Manage your wallet and transactions."
        )

        subtitle.setStyleSheet("""
            color: #94a3b8;
            font-size: 14px;
        """)

        header_text_layout.addWidget(greeting)
        header_text_layout.addWidget(subtitle)

        header_layout.addLayout(header_text_layout)
        header_layout.addStretch()

        # Status
        status = QLabel("●  Online")

        status.setStyleSheet("""
            QLabel {
                color: #4ade80;
                background-color: #163323;
                border-radius: 10px;
                padding: 8px 14px;
                font-size: 12px;
                font-weight: bold;
            }
        """)

        header_layout.addWidget(status)

        content_layout.addLayout(header_layout)

        # ------------------------------------------------------
        # Balance Card
        # ------------------------------------------------------

        balance_card = QFrame()
        balance_card.setMinimumHeight(180)

        balance_card.setStyleSheet("""
            QFrame {
                background-color: #0284c7;
                border-radius: 20px;
            }
        """)

        balance_layout = QVBoxLayout()
        balance_layout.setContentsMargins(30, 25, 30, 25)

        balance_title = QLabel("TOTAL BALANCE")

        balance_title.setStyleSheet("""
            color: #bae6fd;
            font-size: 13px;
            font-weight: bold;
        """)

        balance_layout.addWidget(balance_title)

        self.balance_label = QLabel("$0.00")

        self.balance_label.setStyleSheet("""
            color: white;
            font-size: 42px;
            font-weight: bold;
        """)

        balance_layout.addWidget(self.balance_label)

        balance_layout.addStretch()

        balance_footer = QLabel(
            "Available balance"
        )

        balance_footer.setStyleSheet("""
            color: #bae6fd;
            font-size: 12px;
        """)

        balance_layout.addWidget(balance_footer)

        balance_card.setLayout(balance_layout)

        content_layout.addWidget(balance_card)

        # ------------------------------------------------------
        # Quick Actions
        # ------------------------------------------------------

        actions_title = QLabel("Quick Actions")

        actions_title.setStyleSheet("""
            color: white;
            font-size: 20px;
            font-weight: bold;
        """)

        content_layout.addWidget(actions_title)

        actions_layout = QHBoxLayout()
        actions_layout.setSpacing(15)

        self.deposit_button = self.create_action_button(
            "↓",
            "Deposit",
            "Add money to your wallet"
        )

        self.withdraw_button = self.create_action_button(
            "↑",
            "Withdraw",
            "Withdraw money"
        )

        self.transfer_button = self.create_action_button(
            "↗",
            "Transfer",
            "Send money to another user"
        )

        self.transactions_button = self.create_action_button(
            "↻",
            "Transactions",
            "View your transaction history"
        )

        actions_layout.addWidget(self.deposit_button)
        actions_layout.addWidget(self.withdraw_button)
        actions_layout.addWidget(self.transfer_button)
        actions_layout.addWidget(self.transactions_button)

        content_layout.addLayout(actions_layout)

        # ------------------------------------------------------
        # Bottom section
        # ------------------------------------------------------

        bottom_layout = QHBoxLayout()
        bottom_layout.setSpacing(15)

        # Recent activity
        activity_card = QFrame()

        activity_card.setStyleSheet("""
            QFrame {
                background-color: #1e293b;
                border-radius: 15px;
            }
        """)

        activity_layout = QVBoxLayout()
        activity_layout.setContentsMargins(20, 20, 20, 20)

        activity_title = QLabel("Recent Activity")

        activity_title.setStyleSheet("""
            color: white;
            font-size: 17px;
            font-weight: bold;
        """)

        activity_layout.addWidget(activity_title)

        activity_text = QLabel(
            "No recent transactions."
        )

        activity_text.setStyleSheet("""
            color: #64748b;
            font-size: 13px;
        """)

        activity_layout.addWidget(activity_text)

        activity_layout.addStretch()

        activity_card.setLayout(activity_layout)

        # Security card
        security_card = QFrame()

        security_card.setStyleSheet("""
            QFrame {
                background-color: #1e293b;
                border-radius: 15px;
            }
        """)

        security_layout = QVBoxLayout()
        security_layout.setContentsMargins(20, 20, 20, 20)

        security_title = QLabel("Security")

        security_title.setStyleSheet("""
            color: white;
            font-size: 17px;
            font-weight: bold;
        """)

        security_layout.addWidget(security_title)

        security_status = QLabel(
            "✓ Your session is secure"
        )

        security_status.setStyleSheet("""
            color: #4ade80;
            font-size: 13px;
        """)

        security_layout.addWidget(security_status)

        security_layout.addStretch()

        security_card.setLayout(security_layout)

        bottom_layout.addWidget(activity_card)
        bottom_layout.addWidget(security_card)

        content_layout.addLayout(bottom_layout)

        content.setLayout(content_layout)

        # ======================================================
        # Add everything
        # ======================================================

        main_layout.addWidget(sidebar)
        main_layout.addWidget(content)

        self.setLayout(main_layout)

        # ------------------------------------------------------
        # Button actions
        # ------------------------------------------------------

        self.deposit_button.clicked.connect(self.deposit)
        self.withdraw_button.clicked.connect(self.withdraw)
        self.transfer_button.clicked.connect(self.transfer)
        self.transactions_button.clicked.connect(
            self.show_transactions
        )

    # ==========================================================
    # UI Helpers
    # ==========================================================

    def create_sidebar_button(self, text):

        button = QPushButton(text)

        button.setCursor(Qt.PointingHandCursor)

        button.setMinimumHeight(45)

        button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #94a3b8;
                border: none;
                border-radius: 9px;
                padding: 10px;
                font-size: 13px;
                font-weight: bold;
                text-align: left;
            }

            QPushButton:hover {
                background-color: #26364d;
                color: white;
            }

            QPushButton:pressed {
                background-color: #0284c7;
                color: white;
            }
        """)

        return button

    def create_action_button(
        self,
        icon,
        title,
        description
    ):

        button = QPushButton()

        button.setCursor(Qt.PointingHandCursor)
        button.setMinimumHeight(115)

        button.setStyleSheet("""
            QPushButton {
                background-color: #1e293b;
                border: 1px solid #334155;
                border-radius: 15px;
                text-align: left;
                padding: 15px;
            }

            QPushButton:hover {
                background-color: #26364d;
                border: 1px solid #38bdf8;
            }

            QPushButton:pressed {
                background-color: #0f3b55;
            }
        """)

        layout = QVBoxLayout()
        layout.setSpacing(5)

        icon_label = QLabel(icon)

        icon_label.setStyleSheet("""
            color: #38bdf8;
            font-size: 25px;
            font-weight: bold;
        """)

        title_label = QLabel(title)

        title_label.setStyleSheet("""
            color: white;
            font-size: 14px;
            font-weight: bold;
        """)

        description_label = QLabel(description)

        description_label.setWordWrap(True)

        description_label.setStyleSheet("""
            color: #64748b;
            font-size: 11px;
        """)

        layout.addWidget(icon_label)
        layout.addWidget(title_label)
        layout.addWidget(description_label)

        button.setLayout(layout)

        return button

    # ==========================================================
    # Animation
    # ==========================================================

    def fade_in(self):

        self.opacity_effect = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.opacity_effect)

        self.opacity_animation = QPropertyAnimation(
            self.opacity_effect,
            b"opacity"
        )

        self.opacity_animation.setDuration(600)

        self.opacity_animation.setStartValue(0)
        self.opacity_animation.setEndValue(1)

        self.opacity_animation.setEasingCurve(
            QEasingCurve.OutCubic
        )

        self.opacity_animation.start()

    # ==========================================================
    # Balance Animation
    # ==========================================================

    def update_balance(self, new_balance):

        self.balance = float(new_balance)

        self.balance_animation = QPropertyAnimation(
            self,
            b"windowOpacity"
        )

        self.balance_animation.setDuration(150)

        self.balance_animation.setStartValue(1)
        self.balance_animation.setEndValue(0.7)

        self.balance_animation.finished.connect(
            self.finish_balance_animation
        )

        self.balance_animation.start()

    def finish_balance_animation(self):

        self.balance_label.setText(
            f"${self.balance:,.2f}"
        )

        self.balance_animation = QPropertyAnimation(
            self,
            b"windowOpacity"
        )

        self.balance_animation.setDuration(150)

        self.balance_animation.setStartValue(0.7)
        self.balance_animation.setEndValue(1)

        self.balance_animation.start()

    # ==========================================================
    # Actions
    # ==========================================================

    def deposit(self):

        print("Deposit clicked")

    def withdraw(self):

        print("Withdraw clicked")

    def transfer(self):

        print("Transfer clicked")

    def show_transactions(self):

        print("Transactions clicked")

    # ==========================================================
    # Logout
    # ==========================================================

    def logout(self):

        from pywallet.gui.token_manager import TokenManager

        TokenManager.clear()

        self.logout_requested.emit()

        self.close()