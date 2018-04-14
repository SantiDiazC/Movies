from mongoengine import *


class User(Document):
    name = StringField(max_length=200, required=True)
    nickname = StringField(max_length=10, required=True, unique=True)
    password = StringField(required=True)
