
import os
import redis
from flask import Flask, jsonify

app = Flask(__name__)

cache = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379
)

@app.route("/")
def home():
    try:
        visits = cache.incr("visits")
    except redis.exceptions.ConnectionError:
        visits = "redis not available"

    return jsonify(message="Hello from TaskBoard DevOps", visits=visits)

@app.route("/health")
def health():
    return jsonify(status="ok")
