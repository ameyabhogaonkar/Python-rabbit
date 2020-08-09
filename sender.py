try:
  import pika
except Exception as e:
    print("Some modules are missing {}".format_map(e))

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue="hello")

channel.basic_publish(exchange='',routing_key='hello',body='Hello World')

connection.close()



