from mongoengine import Document, StringField

class Todo(Document):
    name = StringField()
    des = StringField()
    available = StringField(default='No')