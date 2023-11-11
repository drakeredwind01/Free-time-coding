import redis
import subprocess

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
    print("redis not found")
    return False

if __name__ == '__main__':
  if not check_redis_connection():
    print('Redis is not running. Installing Redis...')

    # Install Redis.
    subprocess.run(['sudo', 'apt', 'install', 'redis-server'])

    # Start Redis.
    subprocess.run(['sudo', 'service', 'redis-server', 'start'])

    # Check if Redis is now running.
    if check_redis_connection():
      print('Redis is now running.')
    else:
      print('Failed to start Redis.')
