import pika
from mongoengine import connect

from models import Contact

connect(
    db="mein",
    host="mongodb+srv://remmover:******@cluster0.uhuxtdj.mongodb.net/?retryWrites=true&w=majority"
)

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()


contacts = Contact.objects.all()

for contact in contacts:
    match contact.preferred_contact_method:
        case "email":
            channel.basic_publish(exchange='',
                                  routing_key='email_queue',
                                  body=str(contact.id).encode())
        case "sms":
            channel.basic_publish(exchange='',
                                  routing_key='sms_queue',
                                  body=str(contact.id).encode())

connection.close()
