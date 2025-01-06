# Aqui fica todas as definições do nosso servidor
from flask import Flask
from src.main.routes.calculators import calc_route_bp

app = Flask(__name__)

app.register_blueprint(calc_route_bp) # blueprint cadastrada nas rotas
