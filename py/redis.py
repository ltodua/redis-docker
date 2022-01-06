import redis

agent = redis.Redis(host='localhost', port=6379)

agent.set('hola', 'hello-whoever-you-are')

value = agent.get('hola')

print(value)