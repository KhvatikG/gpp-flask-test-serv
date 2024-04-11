from flask import Flask, request, abort, jsonify
import redis

app = Flask(__name__)
r = redis.Redis()


@app.route('/api_v1/<key>', methods=['GET'])
def get_value(key):
    if key:
        return f'{r.get(key)}'


@app.route('/api_v1/items', methods=['POST'])
def set_value():
    if not request.json:
        abort(400)

    key = request.json.get('key', '')
    value = request.json.get('value', '')

    if key and value:
        r.mset({key: value})

        return jsonify({key: value}), 201
    else:
        abort(400)


@app.route('/api_v1/<key>', methods=['PUT'])
def update_value(key):
    if not request.json:
        abort(400)

    value = request.json.get('value', '')

    if key and value:
        r.mset({key: value})

        return jsonify({key: value}), 201
    else:
        abort(400)


if __name__ == '__main__':
    app.run(debug=True)
