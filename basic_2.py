from flask import Flask

# Instanciando a classe base do Flask
app = Flask('basic_2') #->

# criação da rota
@app.route('/', methods=['GET', 'POST']) #->
def main():
    return "Hello World!"


if __name__ == '__main__':
    app.run()