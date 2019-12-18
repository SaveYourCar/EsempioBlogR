from datetime import datetime

from core.config import db
from core.models.contactsModel import Contacts


def insert_contact(form):
    name = form.get('name')
    email = form.get('email')
    phone = form.get('phone')
    message = form.get('message')
    entry = Contacts(name=name, phone_num=phone, msg=message, date=datetime.now(), email=email)
    db.session.add(entry)
    db.session.commit()