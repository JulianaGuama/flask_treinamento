from flask import Flask, request, jsonify

app = Flask('basic_6')


@app.route('/', methods=['GET', 'POST', 'PUT'])
def main():
    body = request.get_json()

    if request.method == 'GET':
        app.logger.info(' method is GET') #->
        return jsonify(method='GET', body=body, params=request.args, headers=str(request.headers)), 200
    if request.method == 'POST':
        app.logger.info(' method is POST') #->
        app.logger.warning(' not a GET') #->
        return jsonify(method='POST', body=body, params=str(request.args), headers=str(request.headers)), 200
    else:
        app.logger.error(' method is PUT') #->
        return 'erro', 500


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)