import random
import smtplib
from email.message import EmailMessage

class OTP :

    def __init__(self):
        self.code = self.generate_code()

    def generate_code(self):
        code = random.randint(10000 , 99999)
        return code

    def send_email(self , user):
        email = EmailMessage()
        email["From"] = "mahdimohajeri91@gmail.com"
        email["To"] = user.email
        email["Subject"] = "PyWallet OTP"
        email.set_content(
            f'your verfication code is {self.code}'
        )

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()

            smtp.login(
                "your_email@gmail.com",
                "YOUR_APP_PASSWORD"
            )

            smtp.send_message(email)

    def send_sms(self, user):
        pass
