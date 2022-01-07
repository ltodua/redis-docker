from redis import Redis

agent = Redis(host='redis', port=6379)

agent.set('hola', 'hello-whoever-you-are')

value = agent.get('hola')

print(value)