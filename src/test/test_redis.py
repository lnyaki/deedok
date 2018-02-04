import redis

host='localhost'
port=9009

r = redis.StrictRedis(host=host,port=port,db=0)

r.set('foo','HELLO WORLD')

print(r.get('foo'))
