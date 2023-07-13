import sys
import traceback

import pika
from mongoengine import connect

from models import Contact
from bson import ObjectId

connect(
    db="mein",
    host="mongodb+srv://remmover:******@cluster0.uhuxtdj.mongodb.net/?retryWrites=true&w=majority"
)

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()


def send_sms(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contact.objects.get(id=ObjectId(contact_id))
    if not contact.logic_:
        contact.logic_ = True
        contact.save()

    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == '__main__':

    channel.basic_qos(prefetch_count=1)
    channel.queue_declare(queue='sms_queue')
    channel.basic_consume(queue='sms_queue', on_message_callback=send_sms)

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    except Exception:
        channel.stop_consuming()
        traceback.print_exc(file=sys.stdout)
