from flask import render_template, url_for
from flask_mail import Mail, Message
from XRoadsServer.application import app

mail = Mail(app)

sender = app.config["MAIL_USERNAME"]
host = "localhost:5000"


def send_validation_email():
    pass


def send_test():
    msg = Message("Hello",
                  sender="xroads.email.test@gmail.com",
                  recipients=["asouer@gmail.com"])

    mail.send(msg)


def new_test():
    msg = Message(
        'Hello',
        sender='xroads.email.test@gmail.com',
        recipients=
        ['asouer@gmail.com'])
    msg.body = "This is the email body"

    mail.send(msg)


def send_confirmation(email_to: str, nonce: str):
    confirm_msg = Message(
        'XRoads - Email Confirmation',
        sender=sender,
        recipients=[email_to]
    )

    confirm_msg.body = "Confirm Mail"

    validation_url = "http://" + host + url_for('users.validate', nonce=nonce)

    print(validation_url)

    confirm_msg.html = render_template("mailer/confirmation.html", title="Confirmation Email", validation=validation_url)

    mail.send(confirm_msg)


if __name__ == '__main__':
    new_test()
    print(sender)
    send_test()
