from mongoengine import Document, ReferenceField, StringField, connect, ListField
connect(db="mein", host="mongodb+srv://remmover:******@cluster0.uhuxtdj.mongodb.net/?retryWrites=true&w=majority")


class Author(Document):
    fullname = StringField(max_length=100, required=True)
    born_date = StringField(max_length=30, required=True)
    born_location = StringField(max_length=50, required=True)
    description = StringField(required=True)
    meta = {'collection': 'author'}

class Quote(Document):
    tags = ListField(StringField(required=True))
    author = ReferenceField(Author, required=True)
    quote = StringField(required=True)
    meta = {'collection': 'quote'}

