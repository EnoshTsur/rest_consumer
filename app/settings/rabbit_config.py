# user
RABBIT_USER_NAME = 'restaurant'
RABBIT_PASSWORD = '1234'

# vhost
RABBIT_VHOST = 'restaurant_host'

# routing key
REST_NEW_MEAL_ROUTING_KEY = 'rest.new'
REST_STOCK_AMOUNT_ROUTING_KEY = 'rest.amount'
REST_ALL_ROUTING_KEY = 'rest.*'

#queues
REST_NEW_MEAL_QUEUE = 'rest_new_meal_queue'
REST_STOCK_AMOUNT_QUEUE = 'rest_new_meal_queue'
REST_ALL_QUEUE = 'rest_all_queue'

# exchange
TOPIC_EXCHANGE = 'rest.topic'