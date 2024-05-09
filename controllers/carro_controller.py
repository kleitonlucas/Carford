from flask import Blueprint, request

from db.database import db_session as db
from models.carro_model import Carro

carro_route = Blueprint('/carro', __name__)

@carro_route.route('/', methods=['GET'])
def get_all():
    carros = db.query(Carro).all()
    
    response = [
        {
            'id':c.id, 
            'modelo':c.modelo, 
            'placa':c.placa, 
            'cor':c.cor, 
            'proprietario_id':c.proprietario_id
        } for c in carros
    ]
    return response

@carro_route.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    carro = db.query(Carro).get(id)

    if carro:
        response = {
            'id':carro.id, 
            'modelo':carro.modelo, 
            'placa':carro.placa, 
            'cor':carro.cor, 
            'proprietario_id':carro.proprietario_id
        }
    else:
        response = {
            "status": "erro",
            "mensagem": "Carro não encontrado."
        }
    return response

@carro_route.route('/', methods=['POST'])
def post():
    carro = Carro(
        modelo=request.json['modelo'],
        placa=request.json['placa'],
        cor=request.json['cor'],
        proprietario_id=request.json['proprietario_id']
    )

    placa_cadastrada = db.query(Carro).filter_by(placa=carro.placa).first()
    quant_carro_proprietario = db.query(Carro).filter_by(proprietario_id=carro.proprietario_id)

    if placa_cadastrada:
        response = response = {
            "status": "erro",
            "mensagem": "Placa informada já cadastrada."
        }
    elif quant_carro_proprietario.count() >= 3:
        response = response = {
            "status": "erro",
            "mensagem": "Proprietário já atingiu o limite de três carros."
        }
    else:
        db.add(carro)
        db.commit()
        db.refresh(carro)

        response = {
            'id':carro.id, 
            'modelo':carro.modelo, 
            'placa':carro.placa, 
            'cor':carro.cor, 
            'proprietario_id':carro.proprietario_id
        }
    
    return response

@carro_route.route('/<int:id>', methods=['PUT'])
def put(id):
    carro = db.query(Carro).get(id)

    if carro:
        carro.modelo = request.json['modelo']
        carro.placa = request.json['placa']
        carro.cor = request.json['cor']
        carro.proprietario_id = request.json['proprietario_id']

        db.add(carro)
        db.commit()
        db.refresh(carro)

        response = {
            'id':carro.id, 
            'modelo':carro.modelo, 
            'placa':carro.placa, 
            'cor':carro.cor, 
            'proprietario_id':carro.proprietario_id
        }
    else:
        response = {
            "status": "erro",
            "mensagem": "Carro não encontrado."
        }
    
    return response

@carro_route.route('/<int:id>', methods=['DELETE'])
def delete(id):
    carro = db.query(Carro).get(id)

    if carro:
        db.delete(carro)
        db.commit()
        response = {"status": "Sucesso"}
    else:
        response = {
            "status": "erro",
            "mensagem": "Carro não encontrado."
        }
    
    return response