from flask import Flask, request #->

app = Flask('basic_3')


@app.route('/', methods=['GET', 'POST', 'PUT']) #->
def main():
    if request.method == 'GET':
        return 'foi GET', 200
    if request.method == 'POST':
        return 'foi POST', 200
    else:
        return 'erro', 500


if __name__ == '__main__':
    app.run()