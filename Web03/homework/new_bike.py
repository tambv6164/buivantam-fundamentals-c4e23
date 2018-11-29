from mongoengine import Document, StringField, IntField

class New_bike(Document):
    model = StringField()
    dailyfee = IntField()
    image = StringField()
    year = IntField()