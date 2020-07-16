from flask import Flask

# Instanciando a classe base do Flask
app = Flask(__name__) # boa prática: use o nome da aplicação em vez de '__name__'

# criação da rota
@app.route('/')
def main():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
