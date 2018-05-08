from flask import render_template, url_for
from flask_mail import Mail, Message
from XRoadsServer.application import app

mail = Mail(app)

sender = app.config["MAIL_USERNAME"]
host = "localhost:5000"


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
