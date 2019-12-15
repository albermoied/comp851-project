import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='userdatadb')

def send_to_leads(item):
    channel.basic_publish(exchange='', routing_key='leads', body=str(item))

def send_to_high_priority(item):
    channel.basic_publish(exchange='', routing_key='high_priority', body=str(item))

def send_to_txt(item):
    channel.basic_publish(exchange='', routing_key='text_file', body=str(item))
