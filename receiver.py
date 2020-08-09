try:
    import pika
except Exception as e:
    print("Some modules are missing {}".format(e))

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch,method,properties,body):
    print("[x] received %r" %body)

channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print('[*] waiting for message.To exit press ctrl+c')
channel.start_consuming()

