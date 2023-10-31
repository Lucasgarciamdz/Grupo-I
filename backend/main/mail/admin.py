from .. import mailsender
from flask import current_app, render_template
from flask_mail import Message
from smtplib import SMTPException
from main.models import UsuarioModel

def send_new_user_notification_to_admins(new_user):
    try:
        # Consulta la base de datos para obtener a todos los administradores
        admins = UsuarioModel.query.filter_by(rol='admin').all()

        # Construye el cuerpo del correo con los datos del nuevo usuario
        user_info = f"Nuevo usuario registrado:\nNombre: {new_user.nombre}\nEmail: {new_user.email}"

        for admin in admins:
            # Envía el correo a los administradores con los detalles del nuevo usuario
            send_user_info_email(admin.email, 'Nuevo Usuario Registrado', user_info)

        return 'Correo de notificación enviado a los administradores', 200
    except Exception as e:
        print(str(e))
        return 'Error al enviar el correo de notificación', 500

def send_user_info_email(to, subject, user_info):
    msg = Message(subject, sender=current_app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    try:
        msg.body = user_info

        mailsender.send(msg)
    except SMTPException as e:
        print(str(e))
        return "Envío de correo fallido"
    return True
