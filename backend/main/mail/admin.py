from smtplib import SMTPException

from flask import current_app
from flask_mail import Message

from main.models import UsuarioModel
from .. import mailsender


def send_new_user_notification_to_admins(new_user):
    """
    Sends a notification email to all admins when a new user is registered.
    """
    try:
        # Consulta la base de datos para obtener a todos los administradores
        admins = UsuarioModel.query.filter_by(rol='Admin').all()

        # Construye el cuerpo del correo con los datos del nuevo usuario
        user_info = f"Nuevo usuario registrado:\nNombre: {new_user.nombre}\nEmail: {new_user.email}"

        for admin in admins:
            # Envía el correo a los administradores con los detalles del nuevo usuario
            send_user_info_email(admin.email, 'Nuevo Usuario Registrado', user_info)

        return 'Correo de notificación enviado a los administradores', 200
    except SMTPException as e:
        print(e)
        return 'Error al enviar el correo de notificación', 500


def send_user_info_email(to, subject, user_info):
    """
    Sends an email with user information.
    """
    msg = Message(subject, sender=current_app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    try:
        msg.body = user_info
        mailsender.send(msg)
    except SMTPException as e:
        print(e)
        return "Envío de correo fallido"
    return True


def send_new_profesor_notification_to_admins(new_profesor, clase):
    """
    Sends a notification email to all admins when a new professor wants to teach a class.
    """
    try:
        # Query the database to get all the admins
        admins = UsuarioModel.query.filter_by(rol='Admin').all()

        # Build the email body with the new professor's details
        profesor_info = (
            "New professor wants to teach a class:\n"
            f"Professor id: {new_profesor.id_profesor}\n"
            f"Class: {clase.tipo}"
        )

        # Commented out the email sending part
        # for admin in admins:
        #     # Send the email to the admins with the details of the new professor
        #     send_profesor_info_email(admin.email, 'New Professor Class Request', profesor_info)

        return 'Notification email sending skipped', 200
    except Exception as e:
        print(e)
        return 'Failed to process the request', 500


def send_profesor_info_email(to, subject, profesor_info):
    """
    Sends an email with professor information.
    """
    msg = Message(subject, sender=current_app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    try:
        msg.body = profesor_info
        mailsender.send(msg)
    except SMTPException as e:
        print(e)
        return "Email send failed"
    return True
