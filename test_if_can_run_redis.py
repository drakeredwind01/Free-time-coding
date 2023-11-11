import install_redis
import redis
install_redis.install_redis()

def check_redis_connection():
  """Checks if a connection to Redis can be established.

  Returns:
    True if a connection to Redis can be established, False otherwise.
  """

  try:
    r = redis.Redis(host='localhost', port=6379)
    r.ping()
    return True
  except redis.ConnectionError:
    return False

if __name__ == '__main__':
  if check_redis_connection():
    print('Redis is running.')
  else:
    print('Redis is not running.')
