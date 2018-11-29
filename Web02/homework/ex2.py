import mlab
from mongoengine import Document, StringField, IntField
from river import River

mlab.connect()

a = River.objects()
for i in a:
    print(i)
