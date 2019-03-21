from flask import Flask
import redis

app = Flask(__name__)
app.debug = True

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

@app.route('/get/<key>', methods=['GET'])
def get(key):
    result = ''
    key = str(key)
    if r.exists(key) != 0:
        result = r.get(key)
    else:
        result = 'false'
    return result

@app.route('/set/<key>:<value>', methods=['GET'])
def set(key, value):
    key = str(key)
    result = ''
    r.set(key, value)
    if r.exists(key) != 0:
        result = str(value)
    else:
        print('nada')
    return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)