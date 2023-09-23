import redis


r = redis.Redis(host="localhost", port=3030, db=0)
# 3030 is the number for port because we chose 3030 in our docker container using port forwarding.
r.set("name", "Hossein")
