import sys
from app.rabbit.channel import create_channel
from app.rabbit.consume import consume_messages
from app.settings.rabbit_config import TOPIC_EXCHANGE, REST_STOCK_AMOUNT_ROUTING_KEY, REST_STOCK_AMOUNT_QUEUE

if __name__ == '__main__':
    try:
        with create_channel() as channel:
            channel.exchange_declare(
                exchange=TOPIC_EXCHANGE,  # Exchange name
                exchange_type='topic',  # Type of exchange
                durable=True  # Ensure exchange durability
            )

            channel.queue_declare(queue=REST_STOCK_AMOUNT_QUEUE, durable=True)

            channel.queue_bind(
                exchange=TOPIC_EXCHANGE,
                queue=REST_STOCK_AMOUNT_QUEUE,
                routing_key=REST_STOCK_AMOUNT_ROUTING_KEY
            )

            print(f" [*] Waiting for logs in queue: {REST_STOCK_AMOUNT_QUEUE}.")

            channel.basic_consume(
                queue=REST_STOCK_AMOUNT_QUEUE,
                on_message_callback=consume_messages,
                auto_ack=False
            )

            # Start listening for messages
            channel.start_consuming()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
