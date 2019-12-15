import pika, json
from connect import connect

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='text_file')
channel.queue_declare(queue='leads')
channel.queue_declare(queue='high_priority')


def callback_leads(ch, method, properties, body):
    print(" [x] Received leads %r" % body)
    item = json.loads(body)
    connect(item, high_priority=False)

def callback_high_priority(ch, method, properties, body):
    print(" [x] Received high priority %r" % body)
    item = json.loads(body)
    connect(item, high_priority=True)

def callback_txt(ch, method, properties, body):
    print(" [x] Received %r" % body)

    item = json.loads(body)
    #Write the leads into the txt file
    f = open("leads.txt", "a")
    f.write(str(item))
    f.write('\n')
    f.close()

channel.basic_consume(queue='text_file', auto_ack=True, on_message_callback=callback_txt)
channel.basic_consume(queue='leads', auto_ack=True, on_message_callback=callback_leads)
channel.basic_consume(queue='high_priority', auto_ack=True, on_message_callback=callback_high_priority)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
