from flask import Flask
import redis

app = Flask(__name__)
app.debug = True

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

@app.route('/get/<key>', methods=['GET'])
def get(key):
    print(type(key))
    key = str(key)
    if r.get(key):
        result = r.get(key)
    else:
        result = False
    print(str(result) + "\n")
    return result

@app.route('/set/<key>:<value>', methods=['GET'])
def set(key, value):
    key = str(key)
    value = str(value)
    r.set(key, value)
    if r.get(key):
        print(str(key) + " " + str(value))
    else:
        print('nada')
    return value


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3000)