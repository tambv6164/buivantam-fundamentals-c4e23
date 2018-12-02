import mlab
from mongoengine import Document, StringField, IntField
from river import River

mlab.connect()

a = River.objects(continent='Africa')
list1 = []
for i in a:
    list1.append(i.name)

list2 = []
b = River.objects(continent='S. America', length__lt=1000)
for i in b:
    list2.append(i.name)

print('ex2: ', list1)
print('ex3: ', list2)
