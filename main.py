from flask import Flask

from controllers.carro_controller import carro_route
from controllers.proprietario_controller import proprietario_route

app = Flask(__name__)

app.register_blueprint(proprietario_route, url_prefix='/proprietarios')
app.register_blueprint(carro_route, url_prefix='/carros')

if __name__=="__main__":
    app.run()