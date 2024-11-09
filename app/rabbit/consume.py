from pika.adapters.blocking_connection import BlockingChannel
import json

def consume_messages(channel: BlockingChannel, method, props, body):
    # Decode the bytes message and convert it to a dictionary
    message = json.loads(body.decode())

    # Print the converted dictionary
    print("Received message:", message)

    # Acknowledge the message
    channel.basic_ack(method.delivery_tag)