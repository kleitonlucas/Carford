from flask import Blueprint, request

from db.database import db_session as db
from models.proprietario_model import Proprietario

proprietario_route = Blueprint('/proprietario', __name__)

@proprietario_route.route('/', methods=['GET'])
def get_all():
    proprietarios = db.query(Proprietario).all()
    
    response = [
        {
            'id':p.id, 
            'nome':p.nome, 
            'cpf':p.cpf, 
            'endereco':p.endereco, 
            'numero_telefone':p.numero_telefone
        } for p in proprietarios
    ]
    return response

@proprietario_route.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    proprietario = db.query(Proprietario).get(id)

    if proprietario:
        response = {
            'id':proprietario.id,
            'nome':proprietario.nome,
            'cpf':proprietario.cpf,
            'endereco':proprietario.endereco,
            'numero_telefone':proprietario.numero_telefone
        }
    else:
        response = {
            "status": "erro",
            "mensagem": "Proprietário não encontrado."
        }
    
    return response

@proprietario_route.route('/', methods=['POST'])
def post():
    novo_proprietario = Proprietario(
        nome=request.json['nome'],
        cpf=request.json['cpf'],
        endereco=request.json['endereco'],
        numero_telefone=request.json['numero_telefone']
    )

    cpf_cadastrado = db.query(Proprietario).filter_by(cpf=novo_proprietario.cpf).first()

    if not cpf_cadastrado:
        db.add(novo_proprietario)
        db.commit()
        db.refresh(novo_proprietario)

        response = {
            'id':novo_proprietario.id,
            'nome':novo_proprietario.nome,
            'cpf':novo_proprietario.cpf,
            'endereco':novo_proprietario.endereco,
            'numero_telefone':novo_proprietario.numero_telefone
        }
    else:
        response = {
            "status": "erro",
            "mensagem": "CPF já cadastrado."
        }
    
    return response

@proprietario_route.route('/<int:id>', methods=['PUT'])
def put(id):
    proprietario = db.query(Proprietario).get(id)

    if proprietario:
        proprietario.nome = request.json['nome']
        proprietario.cpf = request.json['cpf']
        proprietario.endereco = request.json['endereco']
        proprietario.numero_telefone = request.json['numero_telefone']

        db.add(proprietario)
        db.commit()
        db.refresh(proprietario)

        response = {
            'id':proprietario.id,
            'nome':proprietario.nome,
            'cpf':proprietario.cpf,
            'endereco':proprietario.endereco,
            'numero_telefone':proprietario.numero_telefone
        }
    else:
        response = {
            "status": "erro",
            "mensagem": "Proprietário não encontrado."
        }

    return response

@proprietario_route.route('/<int:id>', methods=['DELETE'])
def delete(id):
    proprietario = db.query(Proprietario).get(id)

    if proprietario:
        db.delete(proprietario)
        db.commit()
        response = {
            "status": "Sucesso"
        }
    else:
        response = {
            "status": "erro",
            "mensagem": "Proprietário não encontrado."
        }

    return response